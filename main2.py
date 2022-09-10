import japanize_kivy # 日本語表示
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.metrics import dp

# ウィンドウサイズの指定
# Window.size = (240, 240)

# アプリの定義
class HelloWorldApp(App):
    # ビルド時に呼ばれる
    def build(self):
        # レイアウトの生成
        self.root = FloatLayout()
       
        # ラベルの追加
        self.label = Label(size_hint = (None, None))
        self.label.bind(size = self.label.setter('text_size'))
        self.label.text = 'ハローワールド' # テキスト
        self.label.font_size = dp(35) # フォントサイズ
        self.label.bold = False # 太字
        self.label.italic = False # イタリック
        self.label.color = (1,1,1,1) # 文字色
        self.label.pos = (dp(0), dp(240-24)) # 位置
        # self.label.size = (dp(1240), dp(20)) # サイズ
        self.label.halign = "left"  # 水平揃え
        self.label.valign = "middle" # 垂直揃え
        self.root.add_widget(self.label)

        # レイアウトを返す
        return self.root

# メインの定義
if __name__ == '__main__':
    HelloWorldApp().run()