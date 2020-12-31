// hide form and display thank you message
function confirmForm() {
  // get form container element
  const formVisible = document.getElementById('formVisible');
  // get form thank you container//
  const formDone = document.getElementById('formDone');

  // switch
  formVisible.style.display = 'none';
  formDone.style.display = 'block';

  // return false to prevent browser default  behavior.
  return false;
}

// sending to home page.
function backToHome() {
  window.location = '/';
}
