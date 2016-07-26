var config = {
  apiKey: "AIzaSyDAdJWY_sP-KiDYzKdgaIcM6JU9YuTLPtE",
  authDomain: "auditoryobscenity.firebaseapp.com",
  databaseURL: "https://auditoryobscenity.firebaseio.com",
  storageBucket: "auditoryobscenity.appspot.com",
};

firebase.initializeApp(config);

firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    console.log(user);
  } else {
    window.location = '/';
  }
});
