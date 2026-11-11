const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');
function closeMenu() {
  toggle.setAttribute('aria-expanded', 'false');
  navigation.classList.remove('is-open');
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('is-open', open);
});
navigation.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    toggle.focus();
  }
});
const notice = document.querySelector('#notice');
function showNotice(title, copy) {
  notice.querySelector('h2').textContent = title;
  notice.querySelector('p').textContent = copy;
  notice.showModal();
}
document.querySelectorAll('[data-pending-page]').forEach(link => link.addEventListener('click', event => {
  event.preventDefault();
  showNotice(link.dataset.pendingPage, 'Work in Progress :)');
}));
document.querySelectorAll('[data-missing-link]').forEach(button => button.addEventListener('click', () => {
  const label = button.dataset.missingLink;
  showNotice(label, 'Work in Progress :)');
}));
document.querySelector('[data-feedback]').addEventListener('click', () => {
  showNotice('Feedback', 'Work in Progress :)');
});
notice.addEventListener('click', event => { if (event.target === notice) notice.close(); });

const tabs = [...document.querySelectorAll('[role="tab"]')];
function selectTab(tab) {
  tabs.forEach(item => {
    const selected = item === tab;
    item.setAttribute('aria-selected', String(selected));
    item.tabIndex = selected ? 0 : -1;
    document.getElementById(item.getAttribute('aria-controls')).hidden = !selected;
  });
}
tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => selectTab(tab));
  tab.addEventListener('keydown', event => {
    let next;
    if (event.key === 'ArrowRight') next = tabs[(index + 1) % tabs.length];
    if (event.key === 'ArrowLeft') next = tabs[(index + tabs.length - 1) % tabs.length];
    if (event.key === 'Home') next = tabs[0];
    if (event.key === 'End') next = tabs[tabs.length - 1];
    if (next) { event.preventDefault(); selectTab(next); next.focus(); }
  });
});

const sponsorForm = document.querySelector('#sponsor-form');
if (sponsorForm) sponsorForm.addEventListener('submit', event => {
  event.preventDefault();
  if (!sponsorForm.reportValidity()) return;
  const values = new FormData(sponsorForm);
  const body = `Name: ${values.get('name')}\nCompany: ${values.get('company')}\nEmail: ${values.get('email')}\nInterested in: ${values.get('interest')}\n\n${values.get('message')}`;
  // The design supplies no form service. Prepare a draft; never claim delivery.
  const draft = document.createElement('a');
  draft.href = `mailto:wie@uwaterloo.ca?subject=${encodeURIComponent('Sponsorship enquiry: ' + values.get('company'))}&body=${encodeURIComponent(body)}`;
  draft.click();
  const status = sponsorForm.querySelector('.form-status');
  status.textContent = 'Your email app will open a draft to wie@uwaterloo.ca. Please review and send it there. This form has not sent your enquiry.';
  status.hidden = false;
});
