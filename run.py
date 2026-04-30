"""
Main application entry point for the portfolio.
"""

from app import create_app

# Top-level WSGI app — required by Vercel's @vercel/python runtime.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
