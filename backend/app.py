from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Tuple
import heapq
from collections import deque

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manual CORS headers middleware
@app.middleware("http")
async def add_cors_header(request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# Handle preflight requests
@app.options("/{path:path}")
async def options_handler(path: str):
    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
        }
    )

# === Models ===
class GridInput(BaseModel):
    grid: List[List[int]]
    start: Tuple[int, int]
    end: Tuple[int, int]

class RadiusInput(BaseModel):
    grid: List[List[int]]
    start: Tuple[int, int]
    radius: int

# === A* Pathfinding ===
def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    open_set = [(0 + heuristic(start, end), 0, start, [start])]
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                neighbor = (nx, ny)
                if neighbor not in visited:
                    heapq.heappush(open_set, (
                        g + 1 + heuristic(neighbor, end),
                        g + 1,
                        neighbor,
                        path + [neighbor]
                    ))
    return []

# === BFS Radius Exploration ===
def bfs_radius(grid: List[List[int]], start: Tuple[int, int], radius: int) -> List[Tuple[int, int]]:
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, 0)])
    visited = set()
    reachable = []

    while queue:
        (x, y), dist = queue.popleft()
        if (x, y) in visited or dist > radius:
            continue
        visited.add((x, y))
        reachable.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                queue.append(((nx, ny), dist + 1))

    return reachable

# === API Endpoints ===
@app.get("/")
def read_root():
    return {"message": "Offline Map Navigator API", "status": "running"}

@app.post("/navigate")
def navigate_grid(data: GridInput):
    try:
        path = a_star(data.grid, data.start, data.end)
        if not path:
            raise HTTPException(status_code=404, detail="No path found")
        return {"path": path, "steps": len(path)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

@app.post("/explore-radius")
def explore_radius(data: RadiusInput):
    try:
        reachable = bfs_radius(data.grid, data.start, data.radius)
        return {"reachable_cells": reachable, "total": len(reachable)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)