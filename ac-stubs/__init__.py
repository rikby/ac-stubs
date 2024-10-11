"""Stub file for mods development in Assetto Corsa"""
#NOTE: Anywhere Type Any is listed- Thats just because I havent figured out the return type yet. 
#NOTE: I am making assumtions based on examples. THis may not be 100% Accurate to each functions use
#NOTE: I have only documented the functions I have found code examples for or enough conversation context on forms/etc to tell me what it does
from typing import Any, Callable

def getCarState(car_identifier, info_identifier, optional_identifier=None):
    """
    Gets the current state of the car
    
    :param car_id: intentifier: int
    :param info_identifier: Any appropriate type
    :param optional_identifier: Any: The optional identifier can be omitted, it is used for special infos where they
                                require a specific tyre, as described in the following section.
    :returns the info_identifier type of information associated to car car_id: intentifier.
    """
    pass


def getDriverName(car_id: int):
    """
    Retrieves the name of the driver associated with a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose driver name is being retrieved.

    Returns:
        str - The name of the driver.
    """


def getTrackName(car_id: int) -> str:
    """
    Retrieves the name of the track associated with a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose track name is being retrieved.

    Returns:
        str - The name of the track.
    """


def getTrackConfiguration(car_id: int) -> str:
    """
    Retrieves the configuration of the track associated with a specified car.

    Parameters:
        car_id: int - The unique identifier of the car whose track configuration is being retrieved.

    Returns:
        str - The configuration details of the track.
    """


def getCarName(car_id: int) -> str:
    """
    Retrieves the name of the car associated with a specified car ID.

    Parameters:
        car_id: int - The unique identifier of the car whose name is being retrieved.

    Returns:
        str - The name of the car.
    """



def getLastSplits(car_id: int): ...


# same as ac.isCarInPitline()
def isCarInPitlane(car_id: int): ...


# same as ac.isCarInPitlane()
def isCarInPitline(car_id: int): ...


# noticed in the SimHub mod
def isCarInPit(car_id: int): ...


def isConnected(car_id: int): ...


def getCarBallast(car_id: int): ...


def getCarMinHeight(car_id: int): ...


def getServerName(): ...


def getServerIP(): ...


def getServerHttpPort(): ...


def getServerSlotsCount(): ...


def getCarsCount(): ...


def getCarLeaderboardPosition(car_id: int): ...


def getCarRealTimeLeaderboardPosition(car_id: int): ...


def getCarFFB(): ...


def setCarFFB(value): ...


def setCameraMode(info_identifier): ...


def getCameraMode(): ...


def isCameraOnBoard(car_id: int): ...


def setCameraCar(camera_id, car_id: int): ...


def getCameraCarCount(car_id: int): ...


def focusCar(car_id: int): ...


def getFocusedCar() -> int: ...


def log(value): ...


def console(value): ...


def newApp(app_name: str) -> Any:
    """
    Creates the app object
    
    Parameters:
        app_name: str - Name of the app

    Returns:
        Any - Object to be passed refrencing the app name(Unknown Type and content)
    """


def setTitle(control_identifier: int, title): ...


def setSize(control_identifier: int, width: int, height: int):
    """
    Sets the size of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        width: int - The width to set for the control element.
        height: int - The height to set for the control element.
    """


def addLabel(control_identifier: int, message: str):
    """
    Adds a label with a specified message to a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        message: str - The message text for the label.
    """


def setPosition(control_identifier: int, x: int, y: int):
    """
    Sets the position of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element
        x: int - The x-coordinate for the control's new position.
        y: int - The y-coordinate for the control's new position.
    """


def setIconPosition(control_identifier: int, x: int, y: int):
    """
    Sets the position of an icon within a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        x: int - The x-coordinate for the icon's new position.
        y: int - The y-coordinate for the icon's new position.
    """


def setTitlePosition(control_identifier: int, x: int, y: int):
    """
    Sets the position of the title within a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        x: int - The x-coordinate for the title's new position.
        y: int - The y-coordinate for the title's new position.
    """


def getPosition(control_identifier: int):
    """
    Retrieves the current position of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
    """


def setText(control_identifier: int, text: str):
    """
    Sets the text content of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element
        text: str - The text content to set for the control element.
    """


def getText(control_identifier: int) -> str:
    """
    Retrieves the current text content of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element.

    Returns:
        str - The current text content of the control element.
    """



def setBackgroundOpacity(control_identifier: int, opacity_percentage: int):
    """Set the background Opacity of the window

    Parameters:
        control_identifier: int - IThe unique identifier of the control element
        opacity_percentage: int - Percentage opacity

    """


def drawBackground(control_identifier: int, value): ...


def drawBorder(control_identifier: int, border_size: int):
    """Draws a border around the window

    Parameters:
        control_identifier: int - The unique identifier of the control element
        border_size: int - size of the border (in pixels)
    """


def setBackgroundTexture(control_identifier: int, path: str):
    """
    Sets the background texture of a control element using the specified file path.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        path: str - The file path to the texture image to be used as the background.
    """


def setFontAlignment(control_identifier: int, alignment): ...


def setBackgroundColor(control_identifier: int, r: int, g: int, b: int): ...


def setVisible(control_identifier: int, value): ...


def addOnAppActivatedListener(control_identifier: int, value): ...


def addOnAppDismissedListener(control_identifier: int, value): ...


def addRenderCallback(control_identifier: int, value): ...


def setFontColor(control_identifier: int, r: int, g: int, b: int, a): ...


def setFontSize(control_identifier: int, value): ...


def initFont(_, fontname, italic, bold): ...


def setCustomFont(control_identifier: int, fontname, italic, bold): ...


def addButton(control_identifier: int, value): ...


def addOnClickedListener(control_identifier: int, value): ...


def addGraph(control_identifier: int, value): ...


def addSerieToGraph(control_identifier: int, r: int, g: int, b: int): ...


def addValueToGraph(control_identifier: int, serie_index, value): ...


def setRange(control_identifier: int, min_value, max_value, max_points=0): ...


def addSpinner(control_identifier: int, value): ...


def setValue(control_identifier: int, value): ...


def getValue(control_identifier: int): ...


def setStep(control_identifier: int, value): ...


def addOnValueChangeListener(control_identifier: int, value): ...


def addProgressBar(control_identifier: int, value): ...


def addTextInput(control_identifier: int, input_name: str): 
    """Adds a text input to the window
    
    Parameters:
        control_identifier: int - ID of the window to add the input to
        input_name: str - Name of the input 
    """


def setFocus(control_identifier: int, focus: int): 
    """
    Sets the focus state of a control element.

    Parameters:
        control_identifier: int - The unique identifier of the control element for which the focus state is being set.
        focus: int - The focus state to set for the control element (e.g., 1 for focused, 0 for unfocused).
    """


def addOnValidateListener(control_identifier: int, OnValidateListener: Callable):
    """
    Adds a validation listener to a control element. The listener is called when validation is required, 
    passing a data string to the listener function.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        OnValidateListener: Callable - The listener function to be called for validation. This function should accept a 
                                    single parameter: data of type str.
    """


def addListBox(control_identifier: int, name): ...


def addItem(control_identifier: int, name): ...


def removeItem(control_identifier: int, id): ...


def getItemCount(control_identifier: int): ...


def setItemNumberPerPage(control_identifier: int, number): ...


def highlightListBoxItem(control_identifier: int, id): ...


def addOnListBoxSelectionListener(control_identifier: int, value): ...


def addOnListBoxDeselectionListener(control_identifier: int, value): ...


def setAllowDeselection(control_identifier: int, allow_deselection): ...


def setAllowMultiSelection(control_identifier: int, allow_multi_selection): ...


def getSelectedItems(control_identifier: int): ...


def addCheckBox(control_identifier: int, value): ...


def addOnCheckBoxChanged(control_identifier: int, value): ...


def addTextBox(control_identifier: int, name): ...


def newTexture(path): ...


def glBegin(primitive_id): ...


def glEnd(): ...


def glVertex2f(x: int, y: int):
    """
    Specifies a vertex in 2D space for rendering in OpenGL.

    Parameters:
    x: int - The x-coordinate of the vertex.
    y: int - The y-coordinate of the vertex.
    """


def glColor3f(r: int, g: int, b: int):
    """
    Sets the color using RGB values for rendering in OpenGL.

    Parameters:
    r: int - The red component of the color (0-255).
    g: int - The green component of the color (0-255).
    b: int - The blue component of the color (0-255).
    """


def glColor4f(r: int, g: int, b: int, a: int):
     """
    Sets the color using RGBA values for rendering in OpenGL.

    Parameters:
        r: int - The red component of the color (0-255).
        g: int - The green component of the color (0-255).
        b: int - The blue component of the color (0-255).
        a: int - The alpha (transparency) component of the color (0-255).
    """


def glQuad(x: int, y:int, width: int, height: int): ...


def glQuadTextured(x: int, y:int, width: int, height: int, texture_id): ...


def isAcLive(): ...


def restart(): ...


def getCarSkin(car_id: int): ...


def getDriverNationCode(car_id: int): ...


def getCurrentSplits(car_id: int): ...


def getTrackLength(car_id: int): ...


def getWindSpeed(): ...


def getWindDirection(): ...


def isAIControlled(): ...


def getCarEngineBrakeCount(): ...


def getCarPowerControllerCount(): ...


def freeCameraSetClearColor(r: int, g: int, b: int, alpha): ...


def freeCameraMoveForward(float): ...


def freeCameraMoveRight(float): ...


def freeCameraMoveUpWorld(float): ...


def freeCameraRotatePitch(float): ...


def freeCameraRotateHeading(float): ...


def freeCameraRotateRoll(float): ...


def sendChatMessage(string_msg: str):
    """
    Sends a chat message with the specified content.

    Parameters:
        string_msg: str - The content of the chat message to be sent.
    """


def addOnChatMessageListener(control_identifier: int, onChatMessage: Callable):
    """
    Adds a chat message listener to a control element. The listener is called when a chat message is received, 
    passing the message content and author to the listener function.

    Parameters:
        control_identifier: int - The unique identifier of the control element.
        onChatMessage: Callable - The listener function to be called when a chat message is received. This function should 
                              accept two parameters: message (str) and author (str).
    """


def getCarRestrictor(car_id: int): ...


def getCarTyreCompound(car_id: int): ...


def getSize(control_identifier: int): ...


def setFont(): ...


def shutdown(): ...
