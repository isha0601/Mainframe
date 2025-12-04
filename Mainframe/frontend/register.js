// Firebase App
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.6.0/firebase-app.js";

// Firebase Auth
import {
  getAuth,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
} from "https://www.gstatic.com/firebasejs/12.6.0/firebase-auth.js";

// Firebase Firestore
import {
  getFirestore,
  setDoc,
  doc,
} from "https://www.gstatic.com/firebasejs/12.6.0/firebase-firestore.js";

// Firebase Analytics (optional)
import { getAnalytics } from "https://www.gstatic.com/firebasejs/12.6.0/firebase-analytics.js";

// Firebase config
const firebaseConfig = {
  apiKey: "AIzaSyCl55RwTtQwPfsNy-KSxU8wJmimicFVabQ",
  authDomain: "mainframe-8075d.firebaseapp.com",
  projectId: "mainframe-8075d",
  storageBucket: "mainframe-8075d.firebasestorage.app",
  messagingSenderId: "920736846588",
  appId: "1:920736846588:web:43be29ec632d2e21897d79",
  measurementId: "G-87GHCHXVK1",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

// Initialize Auth & Firestore
const auth = getAuth(app);
const db = getFirestore(app);

/////////////////////////////////////////////////////////
//  ADMIN LOGIN
document
  .getElementById("admin-login-btn")
  ?.addEventListener("click", async () => {
    const email = document.getElementById("admin-email").value;
    const password = document.getElementById("admin-password").value;

    try {
      const userCred = await signInWithEmailAndPassword(auth, email, password);
      alert("Admin Login Successful!");
      window.location.href = "http://localhost:8501/";
    } catch (err) {
      alert("Login Failed: " + err.message);
    }
  });

/////////////////////////////////////////////////////////
//  ADMIN SIGNUP
document
  .getElementById("admin-signup-btn")
  ?.addEventListener("click", async () => {
    const name = document.getElementById("admin-name").value;
    const email = document.getElementById("admin-email").value;
    const password = document.getElementById("admin-password").value;
    const confirm = document.getElementById("admin-confirm").value;

    if (password !== confirm) {
      alert("Passwords do not match!");
      return;
    }

    try {
      const userCred = await createUserWithEmailAndPassword(
        auth,
        email,
        password
      );

      // Save extra admin details in Firestore
      await setDoc(doc(db, "admins", userCred.user.uid), {
        name,
        email,
        createdAt: new Date(),
      });

      alert("Admin account created successfully!");
      window.location.href = "admin-login.html";
    } catch (err) {
      alert("Signup Failed: " + err.message);
    }
  });

////////////////////////////////////////////////////////
//  user LOGIN
document
  .getElementById("user-login-btn")
  ?.addEventListener("click", async () => {
    const email = document.getElementById("user-email").value;
    const password = document.getElementById("user-password").value;
    try {
      const userCred = await signInWithEmailAndPassword(auth, email, password);
      alert("user Login Successful!");
      window.location.href = "http://localhost:8502/";
    } catch (err) {
      alert("Login Failed: " + err.message);
    }
  });
////////////////////////////////////////////////////////
//  user SIGNUP
document
  .getElementById("user-signup-btn")
  ?.addEventListener("click", async () => {
    const name = document.getElementById("user-name").value;
    const email = document.getElementById("user-email").value;
    const password = document.getElementById("user-password").value;
    const confirm = document.getElementById("user-confirm").value;
    if (password !== confirm) {
      alert("Passwords do not match!");
      return;
    }
    try {
      const userCred = await createUserWithEmailAndPassword(
        auth,
        email,
        password
      );
      // Save extra user details in Firestore
      await setDoc(doc(db, "users", userCred.user.uid), {
        name,
        email,
        createdAt: new Date(),
      });
      alert("user account created successfully!");
      window.location.href = "frontend-user.py";
    } catch (err) {
      alert("Signup Failed: " + err.message);
    }
  });
