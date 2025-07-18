# 🗺️ Offline Map Navigator

A modern, interactive web application for pathfinding and exploration on custom grids. Built with FastAPI backend and vanilla JavaScript frontend, featuring A* pathfinding algorithm and BFS radius exploration.

## 🎥 Demo Video
🔗 [Click here to watch the demo]([https://drive.google.com/file/d/1RVsJ96t_CYDnzQ9Z_ZtRqtROlh0naSlq/view?usp=sharing](https://drive.google.com/file/d/1PD-FQqEJTlX7nPr0NhnnKEwgKqpn66ww/view?usp=sharing))

## ✨ Features

### 🎯 **Pathfinding**
- **A* Algorithm**: Optimal pathfinding with Manhattan distance heuristic
- **Visual Path Display**: Real-time path visualization with smooth animations
- **Obstacle Avoidance**: Navigate around blocked cells efficiently

### 🔍 **Radius Exploration**
- **BFS Algorithm**: Explore all reachable cells within a specified radius
- **Distance-based Search**: Find all accessible locations from any starting point
- **Visual Feedback**: Highlighted reachable areas with pulsing animations

### 🎨 **Interactive Grid Editor**
- **Multiple Grid Sizes**: 5x5 to 20x20 customizable grids
- **Click-to-Edit**: Easy wall placement and removal
- **Visual Modes**: Wall, Start, End, and Clear modes
- **Random Generation**: Auto-generate random obstacle patterns

### 🖥️ **Modern UI**
- **Glassmorphism Design**: Modern blur effects and gradients
- **Responsive Layout**: Works on desktop and mobile devices
- **Real-time Updates**: Instant visual feedback for all operations
- **Status Indicators**: Clear success/error messages

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Modern web browser
- Terminal/Command prompt

### Installation

1. **Clone or download the project files**
   ```bash
   git clone https://github.com/Ammarkarimi/offline_map_navigator
   cd offline-map-navigator
   ```

2. **Install Python dependencies**
   ```bash
   pip install fastapi uvicorn python-multipart
   ```

3. **Start the backend server**
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Open the frontend**
   - Open `index.html` in your web browser
   - Or use a local server like Live Server in VS Code

### Verify Installation
- Backend: Visit `http://localhost:8000/` (should show API info)
- Frontend: Open the HTML file and check the status panel

## 📖 Usage Guide

### Basic Navigation

1. **Set up your grid:**
   - Choose grid size from the dropdown (5x5 to 20x20)
   - Click cells to toggle walls (red = blocked, green = walkable)
   - Use mode buttons to place Start (S) and End (E) points

2. **Find a path:**
   - Click "🧭 Find Path" to calculate optimal route
   - Blue dots show the path from start to end
   - Path length is displayed in the results panel

3. **Explore radius:**
   - Set the exploration radius (1-20)
   - Click "🔍 Explore Radius" to find all reachable cells
   - Green circles show accessible locations

### Advanced Features

- **Random Grid**: Generate random obstacle patterns
- **Clear Grid**: Reset to empty grid
- **API Configuration**: Change backend URL if needed
- **Real-time Stats**: View path length and reachable cell count

## 🔧 API Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

#### Find Path
```http
POST /navigate
Content-Type: application/json

{
  "grid": [[0,0,1],[1,0,0],[0,0,0]],
  "start": [0, 0],
  "end": [2, 2]
}
```

**Response:**
```json
{
  "path": [[0,0],[0,1],[1,1],[2,1],[2,2]],
  "steps": 5
}
```

#### Explore Radius
```http
POST /explore-radius
Content-Type: application/json

{
  "grid": [[0,0,0],[1,0,0],[0,0,0]],
  "start": [0, 0],
  "radius": 3
}
```

**Response:**
```json
{
  "reachable_cells": [[0,0],[0,1],[0,2],[1,1],[1,2],[2,1],[2,2]],
  "total": 7
}
```

#### Health Check
```http
GET /
```

**Response:**
```json
{
  "message": "Offline Map Navigator API is running!",
  "status": "OK",
  "endpoints": ["/navigate", "/explore-radius"]
}
```

## 🏗️ Project Structure

```
offline-map-navigator/
├── app.py              # FastAPI backend server
├── index.html          # Frontend application
└── README.md          # This documentation
```

### Backend (`app.py`)
- FastAPI application with CORS support
- A* pathfinding algorithm implementation
- BFS radius exploration algorithm
- Input validation with Pydantic models

### Frontend (`index.html`)
- Single-page application with vanilla JavaScript
- Interactive grid editor with CSS animations
- Real-time API communication
- Responsive design with modern UI

## 🎨 Customization

### Grid Cell Types
- **🟢 Walkable**: `0` - Open path
- **🔴 Blocked**: `1` - Wall/obstacle
- **🔵 Start**: Special marker for starting position
- **🟠 End**: Special marker for destination
- **🟣 Path**: Calculated route visualization
- **🟡 Reachable**: Cells within exploration radius

### Styling
The frontend uses modern CSS with:
- Glassmorphism effects
- Gradient backgrounds
- Smooth transitions
- Hover animations
- Responsive breakpoints

## 🔧 Troubleshooting

### Common Issues

**CORS Error:**
```
Access to fetch at 'http://localhost:8000/navigate' has been blocked by CORS policy
```
- Ensure the backend includes CORS middleware
- Restart the FastAPI server after code changes
- Check that the API URL in frontend matches backend

**Connection Failed:**
```
TypeError: Failed to fetch
```
- Verify backend is running on port 8000
- Check firewall settings
- Try using `127.0.0.1:8000` instead of `localhost:8000`

**No Path Found:**
```
HTTP 404: No path found
```
- Ensure start and end points are set
- Check that a valid path exists (not blocked by walls)
- Verify start and end points are on walkable cells

### Debug Steps

1. **Check backend status:**
   ```bash
   curl http://localhost:8000/
   ```

2. **Verify API endpoints:**
   Visit `http://localhost:8000/docs` for interactive API documentation

3. **Check browser console:**
   Open Developer Tools (F12) to see JavaScript errors

4. **Test with simple grid:**
   Use a small grid with clear path for testing

## 🚀 Performance Tips

- **Grid Size**: Larger grids (20x20) may have slower pathfinding
- **Radius**: Large exploration radius increases computation time
- **Browser**: Use modern browsers for best performance
- **Local Server**: Use local HTTP server for better file loading

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **A* Algorithm**: Based on Hart, Nilsson, and Raphael's pathfinding algorithm
- **BFS**: Breadth-first search for radius exploration
- **FastAPI**: Modern Python web framework
- **Modern Web Standards**: HTML5, CSS3

## 👨‍💻 Developed By

**Mohammed Ammar Karimi**<br>
💼 [LinkedIn](https://www.linkedin.com/in/mohammed-ammar)<br>
🌐 [Website](https://ammarkarimi.vercel.app/)<br>
📫 [Email](ammarkarimi9898@gmail.com)<br>


---

**Happy Pathfinding!** 🗺️✨
