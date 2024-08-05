import CorobeuClass as crb

ve = 3
vd = 3

robot1 = crb.Corobeu()
robot1.Set_Velocities(ve, vd)
robot1.Wait(3)
robot1.Stop_Robot()