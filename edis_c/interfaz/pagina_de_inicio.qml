import QtQuick 1.1

Rectangle 
{
	id: edis

	property int _padding: (central.width / 4)	
	signal nuevoArchivo

	gradient: Gradient 
	{
         GradientStop { position: 0.1; color: "#d4d4d4" }
         GradientStop { position: 0.5; color: "#232323" }
     }

	Rectangle {
		id: central
		color: "white"
        anchors.fill: parent
        radius: 5
        anchors.margins: parent.height / 40
        smooth: true

		gradient: Gradient 
		{}

		Image {
			id: fondo
			source: "fondo.png"
			anchors.left: parent.left
			anchors.top: parent.top
			opacity: 0.15
			fillMode: Image.PreserveAspectFit
		}

		Text {
			id: saludo
			text: "¡Bienvenido a EDIS-C!"
			anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
			color: "#2e2e2e"
			font.bold: true
   	        font.pointSize: 45
 	        style: Text.Raised
 	        styleColor: "black"	
			}
		Image {
			id: logo
			source: "seiryu.png"
			anchors.horizontalCenter: parent.horizontalCenter
            anchors.top: parent.top
			anchors.topMargin: 60	
			fillMode: Image.PreserveAspectFit
			}	

		Text {
			id: descripcion
			width: 500
			font.pointSize: 13
			anchors.horizontalCenter: parent.horizontalCenter
			anchors.top: logo.bottom
			
			text: "EDIS-C es un Entorno de Desarrollo Integrado para el lenguaje C. Es Software Libre y posee herramientas útiles que le ayudaran en la programación con este lenguaje."
			wrapMode: Text.WordWrap
		}

		Row {
			anchors.horizontalCenter: parent.horizontalCenter
			spacing: parent.width/6
			Button {
				id: boton
				width: 40
				buttonColor: "red"
				height: 35
				label: "Nuevo"
			}
		}

		Text {
		anchors.bottom: parent.bottom
		width: 300
		height: 30
		font.italic: true
		anchors.right: parent.right
		color: "black"
		text: "EDIS-C está escrito en Python"
		}

		Image {
			id: pyLogo
			source: "pylogo.png"
			anchors.bottom: parent.bottom
			anchors.right: parent.right
		}
}

	Text {
		anchors.top: parent.top
		anchors.left: parent.left
		color: "black"
		text: "EDIS-C 2014 - Licencia GPLv3"
		}

	
}