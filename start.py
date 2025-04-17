import os
import voila.app as voila_app

notebook = "Modele_Simulation/Modele_Simulation_Peripherique_Parisien.ipynb"
port = int(os.environ.get("PORT", 8866))  # Render injecte $PORT

voila_app.main([notebook, "--port", str(port), "--no-browser"])