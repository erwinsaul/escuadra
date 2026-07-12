from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication

class WidgetHerramienta(QWidget):
    """
    Clase base para todas las herramientas de la interfaz.
    Proporciona de manera consistente el layout base y el botón
    para copiar los resultados calculados al portapapeles.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self._configurar_interfaz_base()

    def _configurar_interfaz_base(self):
        
        self.layout_principal = QVBoxLayout(self)
        
        # Botón dedicado para copiar resultados
        self.btn_copiar = QPushButton("Copiar resultado")
        self.btn_copiar.clicked.connect(self.copiar_al_portapapeles)
        
        
        self.layout_principal.addWidget(self.btn_copiar)

    def obtener_resultado_formateado(self) -> str:
        """
        Método virtual: Las subclases de cada herramienta específica
        deben sobrescribir este método para devolver el string de su resultado.
        """
        return ""

    def copiar_al_portapapeles(self):
        """
        Obtiene el resultado formateado de la herramienta y lo copia
        al portapapeles del sistema usando QApplication.clipboard.
        """
        resultado = self.obtener_resultado_formateado()
        
        
        if resultado:
            portapapeles = QApplication.clipboard()
            portapapeles.setText(str(resultado))