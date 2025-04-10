# microscope_calculator.py
def real_size(image_size_mm: float, magnification: float) -> float:
    """
    Convert a measured size on the microscope image (mm) to the
    actual specimen size (µm).
    Example: 3 mm at 400× magnification ➜ 7.5 µm
    """
    return (image_size_mm * 1000) / magnification   # mm→µm then divide

if __name__ == "__main__":
    img = float(input("Size on microscope image (mm): "))
    mag = float(input("Objective magnification (×): "))
    print(f"Actual specimen size ≈ {real_size(img, mag):.2f} µm")
