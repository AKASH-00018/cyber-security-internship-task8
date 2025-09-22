# 🔒 Task 8: Keylogger Creation for Educational Use

## 🌟 Objective

This project was developed as part of the Cyber Security Internship to understand the mechanics of **keylogging** using Python. The primary goal is to gain awareness of how attackers capture keystrokes, which is crucial for developing effective detection and prevention strategies. **This tool is for educational and defensive purposes only.**

---

## 🛠️ Tools Used

* **Programming Language:** Python 3
* **Library:** `pynput` (for monitoring keyboard events)
* **Logging:** Python's built-in `logging` module (for saving captured data)

---

## 💻 Implementation Steps

### 1. Project Setup and Dependencies

1.  **Environment:** Ensured Python 3 was installed on the system.
2.  **Library Installation:** Installed the necessary library:
    ```bash
    pip install pynput
    ```

### 2. Keylogger Script (`keylogger.py`)

A Python script was created to handle keyboard events:

* **Logging Configuration:** The `logging` module was configured to write all keystrokes to a file named `log.txt`, including a timestamp for each entry.
* **`on_press` Function:** This callback function was defined to capture two types of keystrokes:
    * Alphanumeric keys (logged as characters).
    * Special keys (logged in a clean format, e.g., `[SPACE]`, `[SHIFT]`).
* **`on_release` Function:** A control mechanism was added using this function. The listener automatically stops when the **'Esc'** key is pressed, ensuring clean exit and log finalization.
* **Listener Start:** The `pynput.keyboard.Listener` was initiated to monitor all system-wide keyboard activity.

### 3. Execution and Demonstration

1.  The script was executed via the terminal:
    ```bash
    python keylogger.py
    ```
2.  While the script was running, a test phrase was typed to generate logs.
3.  The logger was terminated by pressing the **'Esc'** key.

---

## 📝 Deliverables & Results

### A. Source Code

The full code is available in the **`keylogger.py`** file in this repository.

### B. Captured Logs Demonstration

The log data provided below confirms successful capture of keystrokes, including the timing of each key press and proper logging of special keys like `[SPACE]` and `[ESC]`.

**Log Output (`log.txt`):**

The following logs correspond to the user typing the phrase **"my password is 12345678"** and then exiting with **'Esc'**.

| Timestamp | Keystroke |
| :--- | :--- |
| `2025-09-22 16:08:21,842` | `m` |
| `2025-09-22 16:08:22,457` | `y` |
| `2025-09-22 16:08:23,389` | `[SPACE]` |
| `2025-09-22 16:08:24,069` | `p` |
| `2025-09-22 16:08:24,532` | `a` |
| `2025-09-22 16:08:24,986` | `s` |
| `2025-09-22 16:08:25,241` | `s` |
| `2025-09-22 16:08:25,800` | `w` |
| `2025-09-22 16:08:26,144` | `o` |
| `2025-09-22 16:08:26,529` | `r` |
| `2025-09-22 16:08:26,968` | `d` |
| `2025-09-22 16:08:27,492` | `[SPACE]` |
| `2025-09-22 16:08:28,066` | `i` |
| `2025-09-22 16:08:28,864` | `s` |
| `2025-09-22 16:08:29,244` | `[SPACE]` |
| `2025-09-22 16:08:30,637` | `1` |
| `2025-09-22 16:08:31,072` | `2` |
| `2025-09-22 16:08:31,570` | `3` |
| `2025-09-22 16:08:32,074` | `4` |
| `2025-09-22 16:08:32,603` | `5` |
| `2025-09-22 16:08:33,197` | `6` |
| `2025-09-22 16:08:33,702` | `7` |
| `2025-09-22 16:08:34,376` | `8` |
| `2025-09-22 16:08:36,236` | `[ESC]` |

---

## 💡 Key Takeaways & Security Awareness

1.  **Low-Level Access:** Libraries like `pynput` demonstrate how easily an application can hook into low-level operating system events to monitor all user input.
2.  **Stealth and Persistence:** A real-world keylogger would run silently in the background, possibly disguising its process name, and automatically send the logs over the network.
3.  **Defense:** The best defense against software keyloggers includes:
    * **Anti-Virus/Anti-Malware:** Tools that detect suspicious process behavior (Behavioral Monitoring).
    * **Multi-Factor Authentication (MFA):** Even if a password is captured, MFA prevents unauthorized access.
    * **Virtual Keyboards:** Using on-screen keyboards can often bypass software keyloggers, as input is handled by the mouse/screen input, not a physical keystroke event.


# Screenshots:








<img width="1918" height="1079" alt="Screenshot 2025-09-22 161315" src="https://github.com/user-attachments/assets/f50376f4-931d-4460-9c1c-cbeeee8f0adf" />


<img width="1918" height="1078" alt="Screenshot 2025-09-22 161432" src="https://github.com/user-attachments/assets/c85c5acc-8d48-4d9f-8be4-9789ef3666f9" />




