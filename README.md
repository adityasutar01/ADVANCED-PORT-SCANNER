# Advanced Python Port Scanner (with Modern Tkinter GUI)
<p align="center">

  <!-- Python -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python Version">

  <!-- GUI -->
  <img src="https://img.shields.io/badge/GUI-Tkinter-green" alt="Tkinter GUI">

  <!-- Project Status -->
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Project Status">

  <!-- License -->
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">

  <!-- Stars -->
  <img src="https://img.shields.io/github/stars/adityasutar01/ADVANCED-PORT-SCANNER?style=social" alt="GitHub Stars">

  <!-- Forks -->
  <img src="https://img.shields.io/github/forks/adityasutar01/ADVANCED-PORT-SCANNER?style=social" alt="GitHub Forks">
</p>

This project is a fast, user-friendly, and visually modern **Port Scanner** built using Python.  
Instead of running a scanner from the command-line, this tool gives you a **smooth GUI interface** where you can simply enter a target IP, define how many ports you want to scan, and view results instantly inside the app.

It’s designed to help beginners understand how port scanning works internally while giving the project a professional, real-world look.

---

## What This Project Does

This tool scans a target device (like a computer, server, or website) to find **open ports**.  
Open ports are like open doors—services such as SSH, HTTP, FTP, etc. run on them.

Security testers, network engineers, and ethical hackers use port scanners to:

- Identify weak or exposed ports  
- Understand services running on a system  
- Perform network reconnaissance  
- Learn how computers communicate  

This project combines **networking + GUI development + multithreading**, making it a perfect intermediate cybersecurity project.

##  Features (Explained Simply)

###  Modern Dark-Themed GUI  
A neat, beginner-friendly dashboard built using Tkinter with a cyber-style color theme.

###  Fast Multi-Threaded Scanning  
The scanner uses 100 background threads so it scans ports quickly *without freezing the app*.

###  Real-Time Results  
As ports are scanned, results appear live inside a scrolling text area.

###  Simple Inputs  
You only need to enter:
- Target IP  
- Number of ports (example: 1024)

### Fully Responsive  
Even while scanning hundreds of ports, the GUI stays active and responsive.

## Why This Project Is Valuable

This project shows the understanding of:
- Core networking  
- Socket programming  
- Multithreading  
- GUI development  
- Event loops  
- Real-time UI updates  

## Project Structure
    │── port_scanner_gui.py # Main program with GUI + scanner
    │── README.md # Project documentation
    │── requirements.txt # Dependencies (only built-in modules)

## Flowchart 
                 ┌──────────────────────────┐
                 │     Start Application    │
                 └──────────────┬───────────┘
                                │
                                ▼
                 ┌──────────────────────────┐
                 │   Load Tkinter GUI       │
                 └──────────────┬───────────┘
                                │
                                ▼
                 ┌──────────────────────────┐
                 │ User Enters:             │
                 │ - Target IP              │
                 │ - Port Range (1–N)       │
                 └──────────────┬───────────┘
                                │
                                ▼
                 ┌──────────────────────────┐
                 │   User Clicks Scan       │
                 └──────────────┬───────────┘
                                │
                                ▼
                ┌────────────────────────────┐
                │  Start Multi-Thread Engine │
                │  (100 worker threads)      │
                └───────────────┬────────────┘
                                │
                                ▼
              ┌────────────────────────────────┐
              │ Each Thread Scans One Port     │
              │ Using socket.connect_ex()      │
              └───────────────┬────────────────┘
                              │
                              ▼
            ┌────────────────────────────────────┐
            │ If Port == OPEN → Display in GUI   │
            │ Else → Ignore                      │
            └────────────────┬───────────────────┘
                             │
                             ▼
                   ┌────────────────────────────┐
                   │ When Queue Empty → Done    │
                   └──────────────┬─────────────┘
                                  │
                                  ▼
                     ┌──────────────────────────┐
                     │  Show "Scan Completed"   │
                     │  Results remain visible  │
                     └──────────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │        End           │
                         └──────────────────────┘

## How to run
### Steps:
    1. Install Python(Python 3.8+)
    2. Clone this repository
    3. Install Required Libaries:
        pip install -r requirements.txt
    4. Run the program:
        Windows : python port_scanner.py
        Mac : python3 port_scanner.py
    5. Enter Details:
       Target Ip : <your target ip>
       Port Range : Maximum range of port you want to scan

## Author
    Github: 
        github.com/adityasutar01
    Email: 
        sutaraditya68@gmail.com
    linkedin: 
        linkedin.com/in/adityasutar10
    
