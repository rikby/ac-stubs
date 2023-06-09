##
# Stub file for mods development in Assetto Corsa
#

def getCarState(car_identifier, info_identifier, optional_identifier=None):
    """
    :param car_identifier: int
    :param info_identifier: Any appropriate type
    :param optional_identifier: Any: The optional identifier can be omitted, it is used for special infos where they
                                require a specific tyre, as described in the following section.
    :returns the info_identifier type of information associated to car car_identifier.
    """
    pass


def getDriverName(car_id): ...


def getTrackName(car_id): ...


def getTrackConfiguration(car_id): ...


def getCarName(car_id): ...


def getLastSplits(car_id): ...


def log(value): ...


def console(value): ...


def newApp(value): ...


def setTitle(control_identifier, title): ...


def setSize(control_identifier, width, height): ...


def addLabel(control_identifier, value): ...


def setPosition(control_identifier, x, y): ...


def setIconPosition(control_identifier, x, y): ...


def setTitlePosition(control_identifier, x, y): ...


def getPosition(control_identifier): ...


def setText(control_identifier, value): ...


def getText(control_identifier): ...


def setBackgroundOpacity(control_identifier, value): ...


def drawBackground(control_identifier, value): ...


def drawBorder(control_identifier, value): ...


def setBackgroundTexture(control_identifier, path): ...


def setFontAlignment(control_identifier, alignment): ...


def setBackgroundColor(control_identifier, r, g, b): ...


def setVisible(control_identifier, value): ...


def addOnAppActivatedListener(control_identifier, value): ...


def addOnAppDismissedListener(control_identifier, value): ...


def addRenderCallback(control_identifier, value): ...


def setFontColor(control_identifier, r, g, b, a): ...


def addButton(control_identifier, value): ...


def addOnClickedListener(control_identifier, value): ...


def addGraph(control_identifier, value): ...


def addSerieToGraph(control_identifier, r, g, b): ...


def addValueToGraph(control_identifier, serie_index, value): ...


def setRange(control_identifier, min_value, max_value): ...


def addSpinner(control_identifier, value): ...


def setValue(control_identifier, value): ...


def getValue(control_identifier): ...


def setStep(control_identifier, value): ...


def addOnValueChangeListener(control_identifier, value): ...


def addProgressBar(control_identifier, value): ...


def addTextInput(control_identifier, value): ...


def setFocus(control_identifier, focus): ...


def addOnValidateListener(control_identifier, value): ...


def addListBox(control_identifier, name): ...


def addItem(control_identifier, name): ...


def removeItem(control_identifier, id): ...


def getItemCount(control_identifier): ...


def setItemNumberPerPage(control_identifier, number): ...


def highlightListBoxItem(control_identifier, id): ...


def addOnListBoxSelectionListener(control_identifier, value): ...


def addOnListBoxDeselectionListener(control_identifier, value): ...


def setAllowDeselection(control_identifier, allow_deselection): ...


def setAllowMultiSelection(control_identifier, allow_multi_selection): ...


def getSelectedItems(control_identifier): ...


def addCheckBox(control_identifier, value): ...


def addOnCheckBoxChanged(control_identifier, value): ...


def addTextBox(control_identifier, name): ...


def newTexture(path): ...


def glBegin(primitive_id): ...


def glEnd(void): ...


def glVertex2f(x, y): ...


def glColor3f(r, g, b): ...


def glColor4f(r, g, b, a): ...


def glQuad(x, y, width, height): ...


def glQuadTextured(x, y, width, height, texture_id): ...


def isAcLive(): ...


def restart(): ...


# same as ac.isCarInPitline()
def isCarInPitlane(car_id): ...


# same as ac.isCarInPitlane()
def isCarInPitline(car_id): ...


# noticed in the SimHub mod
def isCarInPit(car_id): ...


def getCarSkin(car_id): ...


def getDriverNationCode(car_id): ...


def getCurrentSplits(car_id): ...


def getTrackLength(car_id): ...


def getWindSpeed(): ...


def getWindDirection(): ...


def isAIControlled(): ...


def getCarEngineBrakeCount(): ...


def getCarPowerControllerCount(): ...


def freeCameraSetClearColor(r, g, b, alpha): ...


def freeCameraMoveForward(float): ...


def freeCameraMoveRight(float): ...


def freeCameraMoveUpWorld(float): ...


def freeCameraRotatePitch(float): ...


def freeCameraRotateHeading(float): ...


def freeCameraRotateRoll(float): ...


def sendChatMessage(string_msg): ...


def addOnChatMessageListener(ac_window_id, call_back_function): ...


def getFocusedCar() -> int: ...


def getCarsCount(): ...


def getCarLeaderboardPosition(car_id): ...


def getCarRealTimeLeaderboardPosition(car_id): ...


def isConnected(car_id): ...
