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
      window.location.href = "frontend.py";
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
