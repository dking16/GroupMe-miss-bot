from app import app

if __name__ == "__main__":
    # This part is for running with a development WSGI server like Waitress.
    # For production, Gunicorn or uWSGI would import 'app' directly from this file.
    # Ensure Waitress is installed: pip install waitress
    try:
        from waitress import serve
        print("Starting server with Waitress on http://0.0.0.0:5000")
        serve(app, host='0.0.0.0', port=5000)
    except ImportError:
        print("Waitress not found. Please install it with: pip install waitress")
        print("Falling back to Flask's development server on http://0.0.0.0:5000")
        app.run(host='0.0.0.0', port=5000, debug=True) # Keep debug=True for this fallback
