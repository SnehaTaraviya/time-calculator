I built a time calculator during freeCodeCamp's Scientific Computing with Python course to earn certificate.

The goal of this project is to create a Python function add_time that takes a start time and a duration, then calculates the resulting time, accounting for changes in AM/PM periods and optionally returning the day of the week and the number of days later if specified.

**Implementation Details**

**1. Input Parsing:**
The function accepts three parameters: start (the initial time in 12-hour format with AM/PM), duration (the duration to add in hours and minutes), and an optional args (the starting day of the week).
The start time is split into hours, minutes, and the meridiem (AM/PM) part.
The duration is split into hours and minutes.

**2. Time Calculation:**
Total minutes and hours are calculated by summing the respective components from start and duration.
If the total minutes exceed 60, the excess minutes are converted to hours and added to the total hours.

**3. Hour and Day Adjustment:**
If the total hours exceed 12, the hours are adjusted to fit within the 12-hour format.
The meridiem (AM/PM) is toggled appropriately based on the number of 12-hour cycles.
The number of days passed is calculated based on the number of 24-hour cycles.

**4. Formatting the Result:**
The new time is formatted as a string in the 12-hour format, including the adjusted minutes and meridiem.
If a starting day is provided, the day of the week is adjusted based on the number of days passed.
If the time calculation results in one or more full days passing, this information is appended to the result string.

**5. Output:**
The function returns the new time string, optionally including the updated day of the week and the number of days later.
