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
    T1  = Read ("C0", "Erd_MC_WaterValveEnableActualState",          "01")
    T2  = Write("C0", "Erd_UI_CycleSelection",                       "07")
    T3  = Read ("C0", "Erd_MC_CycleEngineRequestState",        "00 07 05")
    T4  = Read ("C0", "Erd_MC_CycleEngineActualState",            "07 0A")
    T5  = ActionDone("Press and hold the slider in the lidlock")
    T6  = Write("C0", "Erd_MC_CycleEngineRequestState",        "00 07 01") 
    T7  = ActionDone("Wait until you hear a click in the Lidlock and release the slider")
    T8  = Wait (9, "Wait 10 seconds")
    T9 =  ActionPassOrFail("Verify that hot valve turn on")
    T10 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "01")
    T11 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "01") 
    T12 = Wait (9, "Wait 10 seconds")
    T13 = ActionPassOrFail("Verify that hot valve turn off and cold valve turn on")
    T14 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "02")
    T15 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "02")
    T16 = Wait (9, "Wait 10 seconds")
    T17 = ActionPassOrFail("Verify hot valve turn on")
    T18 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "03")
    T19 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "03")
    T20 = Wait (9, "Wait 10 seconds")
    T21 = ActionPassOrFail("Verify Cold and Hot vales shall turn off and drain pump turn on")
    T22 = Read ("C0", "Erd_MC_WaterValvesRequestedState",            "00")
    T23 = Read ("C0", "Erd_WaterValveHardwareActualStates",          "00")
    T24 = Read ("C0", "Erd_MC_DrainPumpRequestedState",           "00 01")
    T25 = Read ("C0", "Erd_MC_DrainPumpActualState",                 "01")
    T26 = Wait (9, "Wait 10 seconds")
    T27 = ActionPassOrFail("Verify drain pump light shall turn off and lick shall unlock")
    T28 = Read ("C0", "Erd_MC_CycleEngineActualState",            "07 0B")
    T29 = Read ("C0", "Erd_MC_LidLockActualState",                   "00") 
    
    return [T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15,
            T16, T17, T18, T19, T20, T21, T22, T23, T24, T25, T26, T27, T28, 
            T29]