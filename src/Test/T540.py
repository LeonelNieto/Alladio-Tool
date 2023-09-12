import sys
import os
Executable_Path = sys.argv[0]
sys.path.append((os.path.dirname(os.path.abspath(Executable_Path))).replace("\\", "/")[0:-5])
from Main import *

def AtTicket()->list[tuple]:
    """
    Automatización de Tickets

    Se debe de colocar una constante antes de los pasos. Ya que esta es la que se tiene que retornar en tupla, como se muestra en el ejemplo

    Returns:
    list[tuple]: Pasos a Automatizar
    """
    T2  = Read ("C0", "Erd_MC_WaterValveEnableActualState",          "01")
    T3  = Write("C0", "Erd_UI_CycleSelection",                       "08")
    T4  = Read ("C0", "Erd_MC_CycleEngineRequestState",        "00 08 05")
    T5  = Read ("C0", "Erd_MC_CycleEngineActualState",            "08 0A")
    T6  = ActionDone("Press and hold the slider in the lidlock")
    T7  = Write("C0", "Erd_MC_CycleEngineRequestState",        "00 08 01") 
    T8  = ActionDone("Wait until you hear a click in the Lidlock and release the slider")
    T9  = Wait (9, "Wait 10 seconds")
    T10 = ActionPassOrFail("Verify that hot valve turn on")
    T11 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "01")
    T12 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "01") 
    T13 = Wait (9, "Wait 10 seconds")
    T14 = ActionPassOrFail("Verify that hot valve turn off and cold valve turn on")
    T15 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "02")
    T16 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "02")
    T17 = Wait (9, "Wait 10 seconds")
    T18 = ActionPassOrFail("Verify hot valve turn on")
    T19 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "03")
    T20 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "03")
    T21 = Wait (9, "Wait 10 seconds")
    T22 = ActionPassOrFail("Verify Cold and Hot vales shall turn off")
    T23 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "00")
    T24 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "00")
    T25 = Wait (9, "Wait 10 seconds")
    T26 = ActionPassOrFail("Verify drain pump light shall turn on")
    T27 = Read ("C0", "Erd_MC_DrainPumpRequestedState",           "00 01")
    T28 = Read ("C0", "Erd_MC_DrainPumpActualState",                 "01")
    T29 = Wait (9, "Wait 10 seconds")
    T30 = ActionPassOrFail("Verify drain pump light shall turn off")
    T31 = ActionPassOrFail("Verify that hear two clicks in the Lidlock")
    T32 = Read ("C0", "Erd_MC_CycleEngineActualState",            "08 0B")
    
    
    return [T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15,
            T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, T26, T27, T28,
            T29, T30, T31, T32]