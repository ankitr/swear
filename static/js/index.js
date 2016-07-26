var config = {
  apiKey: "AIzaSyDAdJWY_sP-KiDYzKdgaIcM6JU9YuTLPtE",
  authDomain: "auditoryobscenity.firebaseapp.com",
  databaseURL: "https://auditoryobscenity.firebaseio.com",
  storageBucket: "auditoryobscenity.appspot.com",
};

firebase.initializeApp(config);

var provider = new firebase.auth.FacebookAuthProvider();

document.querySelector('button').addEventListener('click', function() {
  firebase.auth().signInWithRedirect(provider);
});

firebase.auth().getRedirectResult().then(function(result) {
  window.location = '/quiz';
}).catch(function(error) {
  //TODO(ankitr): pick something prettier than an alert
  alert('You need to be logged into Facebook to take this quiz.');
});
