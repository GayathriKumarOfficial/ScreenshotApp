# ScreenShot_App

A Python-based GUI application to capture screenshots and save them to a specified folder. This project uses `Tkinter` for the graphical interface and `pyautogui` for taking screenshots.

---

## Features

- **Take Screenshots:** Captures the current screen after a 5-second delay.
- **Save Location:** Screenshots are automatically saved in the `D:/PythonProjects/Screenshot/screenshot_pics/` directory.
- **Custom Naming:** Screenshots are saved with unique filenames based on the current timestamp.
- **User-Friendly GUI:** Simple buttons for taking screenshots and quitting the application.

---

## Prerequisites

Before running the application, ensure you have the following installed:

1. **Python 3.6+**
2. Required Python libraries:
   - `pyautogui`
   - `tkinter` (comes pre-installed with Python)

You can install `pyautogui` by running:

```bash
pip install pyautogui
```

---

## How to Run

1. Clone or download the project files.
2. Navigate to the project directory.
3. Run the Python script:
   ```bash
   python screenshot_app.py
   ```
4. The application window will appear with options to take screenshots or quit the app.

---

## Directory Structure

```
ScreenshotApp/
|-- screenshot_app.py         # Main Python script
|-- screenshot_pics/          # Folder where screenshots are saved
```

> **Note:** The `screenshot_pics` directory will be created automatically if it does not exist.

---

## Usage Instructions

1. Launch the application.
2. Click the "Take Screenshot" button.
3. Wait for 5 seconds as the application captures your screen.
4. The screenshot will automatically open and be saved in the `screenshot_pics` directory.
5. To close the application, click the "QUIT" button.

---

## Error Handling

- If the application fails to take a screenshot, an error message will be displayed.
- Ensure that the specified directory (`D:/PythonProjects/Screenshot/screenshot_pics/`) exists or has the necessary permissions.

---

## Future Enhancements

- Add an option to customize the save location through the GUI.
- Include functionality to adjust the delay time before taking a screenshot.
- Implement a preview window for recent screenshots.

---

## License

This project is open-source and free to use. Modify it as needed for your personal or professional projects.

---

## 🤝 Contributions

Feel free to fork and contribute. Open a pull request with your suggestions.

---

## 📩 Contact

For queries: [gayathrikumarofficial@example.com]
LinkedIn:[www.linkedin.com/in/gayathrikumarofficial]



