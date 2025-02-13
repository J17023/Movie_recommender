import "./App.css"; // Importa el archivo CSS

function App() {
  return (
    <div className="center-container">
      {" "}
      {/* Contenedor principal centrado */}
      <div>
        <div className="input-group mb-3">
          <div className="input-group-text">
            <input
              className="form-check-input mt-0"
              type="checkbox"
              value=""
              aria-label="Checkbox for following text input"
            />
          </div>
          <input
            type="text"
            className="form-control"
            aria-label="Text input with checkbox"
          />
        </div>
        <div className="input-group">
          <div className="input-group-text">
            <input
              className="form-check-input mt-0"
              type="radio"
              value=""
              aria-label="Radio button for following text input"
            />
          </div>
          <input
            type="text"
            className="form-control"
            aria-label="Text input with radio button"
          />
        </div>
      </div>
    </div>
  );
}

export default App;
