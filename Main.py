from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (500,500)

screen_helper = """
ScreenManager:
    LoginScreen:
    MenuScreen:
    DaftarScreen:
    SupplierScreen:
    BarangScreen:
    PembeliScreen:
    TransaksiScreen:
    KonfirmasiScreen:
    
<LoginScreen>
    name: 'login'
    MDLabel:
        text: "Login"
        pos_hint: {"center_y": .85}
        font_style: "H3"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: "Selamat Datang Di Halaman Login"
        pos_hint: {"center_y": .75}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDTextField:
        id: username
        hint_text: "Username"
        pos_hint: {"center_x": .5, "center_y": .6}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
    MDTextField:
        id: password
        hint_text: "Password"
        pos_hint: {"center_x": .5, "center_y": .5}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
        password: True
    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x": .5, "center_y": .3}
        size_hint_x: .3
        on_press: root.manager.current = 'menu'
        text_color: 0, 0, 0, 1
    MDRaisedButton:
        text: "Sign Up !"
        pos_hint: {"center_x": .5, "center_y": .1}
        size_hint_x: .2
        on_press: root.manager.current = 'daftar'
        text_color: 0, 0, 0, 1
        
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Supplier'
        pos_hint: {'center_x':0.5,'center_y':0.7}
        on_press: root.manager.current = 'Supplier'
    MDRectangleFlatButton:
        text: 'Barang'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'Barang'
    MDRectangleFlatButton:
        text: 'Pembeli'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'Pembeli'
    MDRectangleFlatButton:
        text: 'Transaksi'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'Transaksi'
    MDRectangleFlatButton:
        text: 'Logout'
        pos_hint: {'center_x':0.8,'center_y':0.2}
        on_press: root.manager.current = 'login'

<DaftarScreen>:
    name: 'daftar'
    MDLabel:
        text: "Daftar"
        pos_hint: {"center_y": .85}
        font_style: "H3"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: "Silahkan Masukan Data Anda"
        pos_hint: {"center_y": .75}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDTextField:
        id: nama
        hint_text: "Nama Lengkap"
        pos_hint: {"center_x": .5, "center_y": .6}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
    MDTextField:
        id: email
        hint_text: "Alamat Email"
        pos_hint: {"center_x": .5, "center_y": .5}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
        password: True
    MDTextField:
        id: password
        hint_text: "Masukan Password"
        pos_hint: {"center_x": .5, "center_y": .4}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: .8
        password: True
    MDRaisedButton:
        text: "Daftar !"
        pos_hint: {"center_x": .5, "center_y": .1}
        size_hint_x: .3
        on_press: root.manager.current = 'konfirmasi'
        text_color: 0, 0, 0, 1
    
<KonfirmasiScreen>:
    name: 'konfirmasi'
    MDLabel:
        text: "Selamat Anda Sudah Terdaftar"
        pos_hint: {"center_y": .85}
        font_style: "H3"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDRaisedButton:
        text: "Next !"
        pos_hint: {"center_x": .5, "center_y": .1}
        size_hint_x: .3
        on_press: root.manager.current = 'menu'
        text_color: 0, 0, 0, 1
    
<SupplierScreen>:
    name: 'Supplier'
    MDLabel:
        text: "Entri Supplier"
        pos_hint: {"center_y": 0.9}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: 'Id Supplier'
        pos_hint: {'center_x':0.6,'center_y':0.7}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.7}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Nama Supplier'
        pos_hint: {'center_x':0.6,'center_y':0.6}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.6}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'No Telp'
        pos_hint: {'center_x':0.6,'center_y':0.5}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.5}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Alamat'
        pos_hint: {'center_x':0.6,'center_y':0.4}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.4}
        size_hint: (.2, None)
        height: 30
    MDRectangleFlatButton:
        text: 'Simpan'
        pos_hint: {'center_x':0.4,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
<BarangScreen>:
    name: 'Barang'
    MDLabel:
        text: "Entri Barang"
        pos_hint: {"center_y": 0.9}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: 'Id Barang'
        pos_hint: {'center_x':0.6,'center_y':0.7}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.7}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Id Supplier'
        pos_hint: {'center_x':0.6,'center_y':0.6}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.6}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Nama Barang'
        pos_hint: {'center_x':0.6,'center_y':0.5}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.5}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Harga Barang'
        pos_hint: {'center_x':0.6,'center_y':0.4}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.4}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Stok Barang'
        pos_hint: {'center_x':0.6,'center_y':0.3}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.3}
        size_hint: (.2, None)
        height: 30
    MDRectangleFlatButton:
        text: 'Simpan'
        pos_hint: {'center_x':0.4,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
<PembeliScreen>:
    name: 'Pembeli'
    MDLabel:
        text: "Entri Pembeli"
        pos_hint: {"center_y": 0.9}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: 'Id Pembeli'
        pos_hint: {'center_x':0.6,'center_y':0.7}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.7}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Nama Pembeli'
        pos_hint: {'center_x':0.6,'center_y':0.6}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.6}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Jenis Kelamin'
        pos_hint: {'center_x':0.6,'center_y':0.5}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.5}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'No Telp'
        pos_hint: {'center_x':0.6,'center_y':0.4}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.4}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Alamat'
        pos_hint: {'center_x':0.6,'center_y':0.3}
    TextInput:
        pos_hint: {'center_x':0.7,'center_y':0.3}
        size_hint: (.2, None)
        height: 30
    MDRectangleFlatButton:
        text: 'Simpan'
        pos_hint: {'center_x':0.4,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'menu'
      
<TransaksiScreen>:
    name: 'Transaksi'
    MDLabel:
        text: "Entri Transaksi"
        pos_hint: {"center_y": 0.9}
        font_style: "H5"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0, 0, 0, 1
    MDLabel:
        text: 'Id Transaksi'
        pos_hint: {'center_x':0.5,'center_y':0.7}
    TextInput:
        pos_hint: {'center_x':0.4,'center_y':0.7}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Id Pembeli'
        pos_hint: {'center_x':1.0,'center_y':0.7}
    TextInput:
        pos_hint: {'center_x':0.8,'center_y':0.7}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Nama Barang'
        pos_hint: {'center_x':0.5,'center_y':0.6}
    TextInput:
        pos_hint: {'center_x':0.4,'center_y':0.6}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Jumlah Barang'
        pos_hint: {'center_x':0.5,'center_y':0.5}
    TextInput:
        pos_hint: {'center_x':0.4,'center_y':0.5}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Harga Barang'
        pos_hint: {'center_x':0.5,'center_y':0.4}
    TextInput:
        pos_hint: {'center_x':0.4,'center_y':0.4}
        size_hint: (.2, None)
        height: 30
    MDLabel:
        text: 'Total Bayar'
        pos_hint: {'center_x':0.5,'center_y':0.3}
    TextInput:
        pos_hint: {'center_x':0.4,'center_y':0.3}
        size_hint: (.2, None)
        height: 30
    MDRectangleFlatButton:
        text: 'Simpan'
        pos_hint: {'center_x':0.4,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.8,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
"""

class LoginScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class DaftarScreen(Screen):
    pass


class SupplierScreen(Screen):
    pass

class BarangScreen(Screen):
    pass

class PembeliScreen(Screen):
    pass

class TransaksiScreen(Screen):
    pass

class KonfirmasiScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='login'))
sm.add_widget(MenuScreen(name='daftar'))
sm.add_widget(MenuScreen(name='konfirmasi'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SupplierScreen(name='Supplier'))
sm.add_widget(BarangScreen(name='Barang'))
sm.add_widget(PembeliScreen(name='Pembeli'))
sm.add_widget(TransaksiScreen(name='Transaksi'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()