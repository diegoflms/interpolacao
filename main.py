from internal.controllers.main_controller import MainController

ctrl = MainController()
image_path = 'diego.png'

ctrl.carregarImg(image_path)

ctrl.rotacionarImg(90)

ctrl.zoomImg(2)


