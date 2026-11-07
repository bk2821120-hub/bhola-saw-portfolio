/* ============================================================
   Portfolio CMS — Admin Panel JavaScript
   ============================================================ */

// -- Sidebar toggle (mobile) --------------------------------
const hamburger = document.getElementById('admin-hamburger');
const sidebar   = document.getElementById('admin-sidebar');
const overlay   = document.getElementById('admin-overlay');

if (hamburger && sidebar) {
  hamburger.addEventListener('click', () => {
    sidebar.classList.toggle('open');
    overlay.classList.toggle('active');
  });
  overlay?.addEventListener('click', () => {
    sidebar.classList.remove('open');
    overlay.classList.remove('active');
  });
}

// -- Active nav link ----------------------------------------
const currentPath = window.location.pathname;
document.querySelectorAll('.admin-nav-link').forEach(link => {
  if (link.getAttribute('href') && currentPath.startsWith(link.getAttribute('href'))) {
    link.classList.add('active');
  }
});

// -- Confirm delete dialogs --------------------------------
document.querySelectorAll('.confirm-delete').forEach(form => {
  form.addEventListener('submit', e => {
    if (!confirm('Are you sure you want to delete this? This action cannot be undone.')) {
      e.preventDefault();
    }
  });
});

// -- Auto-dismiss admin alerts ------------------------------
document.querySelectorAll('.admin-alert').forEach(alert => {
  setTimeout(() => {
    alert.style.transition = 'opacity 0.4s';
    alert.style.opacity = '0';
    setTimeout(() => alert.remove(), 400);
  }, 4500);
});

// -- Toggle field visibility (e.g. end_date when currently_working) --
const currentlyWorking = document.getElementById('id_currently_working');
const endDateGroup = document.getElementById('end-date-group');
if (currentlyWorking && endDateGroup) {
  const toggleEnd = () => {
    endDateGroup.style.display = currentlyWorking.checked ? 'none' : 'block';
  };
  toggleEnd();
  currentlyWorking.addEventListener('change', toggleEnd);
}

// -- File input preview ------------------------------------
document.querySelectorAll('input[type="file"][data-preview]').forEach(input => {
  const previewId = input.dataset.preview;
  const preview = document.getElementById(previewId);
  if (!preview) return;
  input.addEventListener('change', () => {
    const file = input.files[0];
    if (!file) return;
    if (file.type.startsWith('image/')) {
      const reader = new FileReader();
      reader.onload = e => { preview.src = e.target.result; preview.style.display = 'block'; };
      reader.readAsDataURL(file);
    }
  });
});

// -- Form loading state ------------------------------------
document.querySelectorAll('form.admin-form').forEach(form => {
  form.addEventListener('submit', function() {
    if (typeof this.checkValidity === 'function' && !this.checkValidity()) return;
    const btn = this.querySelector('button[type="submit"]');
    if (btn) {
      setTimeout(() => {
        btn.innerHTML = '<span class="spinner-border spinner-border-sm me-1"></span> Saving…';
        btn.disabled = true;
      }, 0);
    }
  });
});

// ============================================================
// -- Bootstrap Icon Auto-Extractor, Live Preview & Picker ----
// ============================================================
(function() {
  function extractBootstrapIcon(raw) {
    if (!raw) return '';
    raw = raw.trim();

    // 1. Extract class from HTML tag <i class="bi bi-linkedin"></i> or <span class="bi-github">
    const htmlClassMatch = raw.match(/class=["']([^"']+)["']/i);
    if (htmlClassMatch) {
      const classes = htmlClassMatch[1].split(/\s+/);
      const biClass = classes.find(c => c.startsWith('bi-'));
      if (biClass) return biClass;
      const nonBi = classes.find(c => c !== 'bi');
      if (nonBi) return nonBi.startsWith('bi-') ? nonBi : `bi-${nonBi}`;
    }

    // 2. Handle stripped/pasted string like "bi bi-linkedin" or "<i bi-linkedin>"
    const tagStripped = raw.replace(/[<>/]/g, '').trim();
    const tokens = tagStripped.split(/\s+/);
    const biToken = tokens.find(t => t.startsWith('bi-'));
    if (biToken) return biToken;

    // 3. Direct class name "bi-linkedin"
    if (raw.startsWith('bi-')) return raw;

    // 4. Raw platform name like "linkedin" -> "bi-linkedin"
    if (/^[a-z0-9_-]+$/i.test(raw) && !raw.startsWith('bi-')) {
      return `bi-${raw}`;
    }

    return raw;
  }

  const platformIconMap = {
    'github': 'bi-github',
    'linkedin': 'bi-linkedin',
    'twitter': 'bi-twitter-x',
    'youtube': 'bi-youtube',
    'instagram': 'bi-instagram',
    'facebook': 'bi-facebook',
    'kaggle': 'bi-trophy',
    'email': 'bi-envelope',
    'other': 'bi-link-45deg'
  };

  const iconInputs = document.querySelectorAll('#id_icon, .icon-picker-input, input[name="icon"]');

  iconInputs.forEach(input => {
    const container = input.closest('.col-md-6, .col-md-4, .admin-form-group, .icon-input-wrapper') || input.parentElement;
    const previewBox = container ? container.querySelector('.icon-preview-box') : document.getElementById('icon-preview');
    const previewIcon = previewBox ? previewBox.querySelector('i') : null;
    const feedbackElem = container ? container.querySelector('.icon-detected-badge') : null;

    function applyIcon(val, wasPaste = false) {
      const cleanClass = extractBootstrapIcon(val);
      if (cleanClass !== val && (val.includes('<') || val.includes('bi ') || val.includes('"'))) {
        input.value = cleanClass;
        if (feedbackElem) {
          feedbackElem.innerHTML = `<i class="bi bi-magic me-1"></i> Auto-extracted: <code>${cleanClass}</code>`;
          feedbackElem.style.display = 'inline-flex';
          setTimeout(() => { feedbackElem.style.display = 'none'; }, 3500);
        }
      }

      if (previewIcon) {
        if (cleanClass) {
          previewIcon.className = `bi ${cleanClass}`;
          if (previewBox) previewBox.classList.add('has-icon');
        } else {
          previewIcon.className = 'bi bi-app';
          if (previewBox) previewBox.classList.remove('has-icon');
        }
      }

      // Highlight active chip if present
      document.querySelectorAll('.icon-chip').forEach(chip => {
        const chipVal = chip.dataset.icon || chip.innerText.trim();
        if (chipVal === cleanClass || `bi-${chipVal}` === cleanClass) {
          chip.classList.add('active');
        } else {
          chip.classList.remove('active');
        }
      });
    }

    input.addEventListener('input', () => applyIcon(input.value));
    input.addEventListener('change', () => applyIcon(input.value));
    input.addEventListener('paste', () => {
      setTimeout(() => applyIcon(input.value, true), 10);
    });

    // Initial render
    if (input.value) {
      applyIcon(input.value);
    }
  });

  // Quick Chips Click Event
  document.querySelectorAll('.icon-chip').forEach(chip => {
    chip.addEventListener('click', function(e) {
      e.preventDefault();
      const iconVal = this.dataset.icon;
      const targetInput = document.querySelector('#id_icon, .icon-picker-input, input[name="icon"]');
      if (targetInput && iconVal) {
        targetInput.value = iconVal;
        targetInput.dispatchEvent(new Event('input', { bubbles: true }));
      }
    });
  });

  // Platform dropdown auto-selection
  const platformSelect = document.getElementById('id_platform');
  if (platformSelect) {
    platformSelect.addEventListener('change', function() {
      const selectedPlat = this.value;
      const targetInput = document.querySelector('#id_icon, .icon-picker-input');
      if (targetInput && platformIconMap[selectedPlat]) {
        // Only override if empty or currently a platform default icon
        const current = targetInput.value.trim();
        const isKnownDefault = Object.values(platformIconMap).includes(current);
        if (!current || isKnownDefault) {
          targetInput.value = platformIconMap[selectedPlat];
          targetInput.dispatchEvent(new Event('input', { bubbles: true }));
        }
      }
    });
  }

  // Modal Icon Search & Selection
  const iconSearchInput = document.getElementById('iconModalSearch');
  if (iconSearchInput) {
    iconSearchInput.addEventListener('input', function() {
      const q = this.value.toLowerCase().trim();
      document.querySelectorAll('.icon-picker-item').forEach(item => {
        const name = (item.dataset.name || item.innerText).toLowerCase();
        const icon = (item.dataset.icon || '').toLowerCase();
        if (!q || name.includes(q) || icon.includes(q)) {
          item.style.display = 'flex';
        } else {
          item.style.display = 'none';
        }
      });
    });
  }

  document.querySelectorAll('.icon-picker-item').forEach(item => {
    item.addEventListener('click', function() {
      const iconVal = this.dataset.icon;
      const targetInput = document.querySelector('#id_icon, .icon-picker-input, input[name="icon"]');
      if (targetInput && iconVal) {
        targetInput.value = iconVal;
        targetInput.dispatchEvent(new Event('input', { bubbles: true }));
      }
      // Close modal if bootstrap is active
      const modalEl = document.getElementById('iconPickerModal');
      if (modalEl && typeof bootstrap !== 'undefined' && bootstrap.Modal) {
        const modal = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
        modal.hide();
      }
    });
  });
})();
