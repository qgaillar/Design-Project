import os
import voila.app as voila_app

print("DEBUG: $PORT =", os.environ.get("PORT"))

notebook = "Modele_Simulation/Modele_Simulation_Peripherique_Parisien.ipynb"
port = int(os.environ.get("PORT", "8888"))  # fallback à 8888 au cas où

voila_app.main([
    notebook,
    "--port", str(port),
    "--no-browser",
    "--Voila.base_url=/"
])