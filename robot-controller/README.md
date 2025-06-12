# Robot Controller Project

This project implements a robot controller using Python. It includes a web interface to display the robot's coordinates in real-time.

## Project Structure

```
robot-controller
├── src
│   ├── controller.py       # Main logic for controlling the robot
│   ├── web
│   │   ├── app.py          # Flask web application
│   │   └── templates
│   │       └── index.html  # HTML template for displaying coordinates
│   └── utils.py            # Utility functions for the robot
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd robot-controller
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask web application:
   ```
   python src/web/app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000` to view the robot's coordinates.

## Usage

- The robot can be controlled through the methods defined in `controller.py`. 
- The web application will display the current coordinates of the robot and update them periodically.

## Additional Information

- Ensure that the robot is properly connected and configured before running the application.
- Modify the `controller.py` file to implement specific movement logic for the robot as needed.