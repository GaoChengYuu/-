import openvsp as vsp

# 创建一个新的OpenVSP模型
model = vsp.VSPModel()

# 添加几何体
wing = model.AddGeom("WING")
wing.SetDriver("Span", "2.5")

# 设置几何体属性
wing.SetParmVal("X_Rel_Location", 0.0, 0)
wing.SetParmVal("Y_Rel_Location", 0.0, 0)
wing.SetParmVal("Z_Rel_Location", 0.0, 0)

# 保存模型
model.SaveVSP("my_model.vsp3")