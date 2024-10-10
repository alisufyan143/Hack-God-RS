```markdown
# GUI Scientific Calculator

This project is a graphical user interface (GUI) scientific calculator implemented in Python using the `Tkinter` library. The calculator can perform basic arithmetic operations as well as advanced scientific calculations, including trigonometric, logarithmic, and exponential functions.

## Features

- **Basic Calculator Operations:**
  - Addition, Subtraction, Multiplication, and Division
  - Clear last entry (`C`) and All Clear (`AC`)

- **Scientific Calculator Operations:**
  - Trigonometric functions: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
  - Logarithmic functions: `ln` (natural log), `log` (base-10)
  - Factorial: `x!`
  - Square root: `√`
  - Exponentiation: `^`
  - Reciprocal: `1/x`
  - Degree and Radian conversion: `deg`, `rad`
  - Pi (`π`)

## Project Structure

- **`main.py`**: Contains the main code for the calculator application, including both the basic and scientific functionalities.
- **Dependencies**: The project only relies on the built-in Python libraries (`Tkinter` and `math`).

## How to Run

### Prerequisites

Ensure you have Python installed on your system. This project uses the following Python libraries:

- `Tkinter` (usually pre-installed with Python)
- `math` (built-in library)

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/scientific-calculator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd scientific-calculator
   ```

3. Run the `main.py` file:

   ```bash
   python main.py
   ```

The calculator window will appear, allowing you to perform various operations.

## Usage

1. **Basic Mode**:
   - The calculator starts in basic mode with numerical buttons (0-9) and basic operations (`+`, `-`, `×`, `÷`).
   - Use the buttons or your keyboard to enter values and perform operations.

2. **Scientific Mode**:
   - To switch to scientific mode, go to `Mode > Scientific Calculator` in the menu bar.
   - Scientific buttons like `sin`, `cos`, `log`, etc., will appear.
   - Enter your desired values and click on any scientific button to see the result.

3. **Switching Between Modes**:
   - Use the menu bar to switch between basic and scientific modes without losing the current state.

## Customization

You can customize the calculator's appearance by modifying the properties in the `main.py` file:

- **Button Colors**: Change the `bg` and `fg` parameters.
- **Font Styles**: Modify the `font` parameter for buttons and display.
- **Layout**: Adjust the frame and grid layout to personalize the interface.

## Contribution

Contributions are welcome! If you'd like to contribute to the project:

1. Fork the repository.
2. Create a new branch with your feature/fix: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request to the `main` branch.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Muhammad Ahmad** - [GitHub](https://github.com/username1)
- **Muhammad Ali Sufyan** - [GitHub](https://github.com/username2)

## Acknowledgments

- Thanks to [Python Documentation](https://docs.python.org/3/library/tkinter.html) for guidance on using Tkinter.
- Inspiration and code structure based on various open-source calculator projects.
```

### Tips:
1. **Update the links**: Replace `https://github.com/your-username/scientific-calculator.git` with the actual GitHub URL of your repository.
2. **Add Screenshots**: Create a `screenshots` folder in your repository and add images of your calculator in both basic and scientific modes, then link them in the `Screenshots` section.
3. **Edit the Authors Section**: Replace `username1` and `username2` with your actual GitHub usernames.

This `README.md` should give users a clear understanding of your project, its functionality, and how to use it. Let me know if you'd like to include additional details or if there's anything specific you want to highlight!
