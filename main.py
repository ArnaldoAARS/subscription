import stripe
from stripe.error import InvalidRequestError
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

stripe.api_key = 'sk_test_51KuiHoJTbZoKzQ84SkzUDxOiYjYMu92VeJshz1IWepvHyDHarulAAXoudZ41qRYulSBXSYABZU6EfgnDZPQB9QU600ErEzsmtu'


class AARS(App):
    def build(self):
        self.window = GridLayout()
        #add widgets to window
        self.window.cols = 1
        self.window.size_hint=(0.4, 1)
        self.window.pos_hint={"center_x": 0.5, "center_y": 0.5}


        self.window.add_widget(Image(source='AARS_Logo.png'))

        self.nombre = Label(
                    text="Name",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.nombre)


        self.usernombre=TextInput(
            
            multiline=False,
            size_hint = (1,0.5),
            padding_y=(2,2)
            ) 
        self.window.add_widget(self.usernombre)



        

        self.phone = Label(
                    text="Phone",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.phone)


        self.userphone=TextInput(
            padding_y=(2,2),
            multiline=False,
            size_hint = (1,0.5)
            ) 
        self.window.add_widget(self.userphone)


        self.address = Label(
                    text="Address",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.address)


        self.useraddress=TextInput(
            padding_y=(2,2),
            multiline=False,
            size_hint = (1,0.5)
            ) 
        self.window.add_widget(self.useraddress)



        
        self.email = Label(
                    text="Email",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.email)


        self.useremail=TextInput(
            padding_y=(2,2),
            multiline=False,
            size_hint = (1,0.5)
            ) 
        self.window.add_widget(self.useremail)




        #TArjeta

        self.cardnum = Label(
                    text="Card Number",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.cardnum)


        self.usercard=TextInput(
            padding_y=(2,2),
            multiline=False,
            size_hint = (1,0.5)
            ) 
        self.window.add_widget(self.usercard)  







        self.month = Label(
                    text="Month",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.month)


        self.userm=TextInput(
            padding_y=(2,2),
            multiline=False,
            size_hint = (1,0.5)
            ) 
        self.window.add_widget(self.userm)



        self.year = Label(
                    text="Year",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.year)


        self.usery=TextInput(
            padding_y=(2,2),
            multiline=False,
            size_hint = (1,0.5)
            ) 
        self.window.add_widget(self.usery)
        

        




        self.cvv = Label(
                    text="CVV",
                    font_size =18,
                    color = '#83DADC'
                    )
        self.window.add_widget(self.cvv)


        self.usercvv=TextInput(
            padding_y=(2,2),
            multiline=False,
            size_hint = (1,0.5)
            ) 
        self.window.add_widget(self.usercvv)



        self.button=Button(
            text='Send inf',
            size_hint = (1,0.5),
            bold= True,
            background_color = '#83DADC',
            background_normal = ""

            )
        
        self.button.bind(on_press=self.callback)

        self.window.add_widget(self.button)
        
        
        return self.window



    
    
    
    
    def callback(self, instance):
        
        stripe.api_key = 'sk_test_51KuiHoJTbZoKzQ84SkzUDxOiYjYMu92VeJshz1IWepvHyDHarulAAXoudZ41qRYulSBXSYABZU6EfgnDZPQB9QU600ErEzsmtu'


        try:
            
        
            token1= stripe.Token.create(
            card={
                "number": self.usercard.text,
                "exp_month": self.userm.text,
                "exp_year": self.usery.text,
                "cvc": self.usercvv.text,
            },
              )
            

            stripe.Customer.create(
                name=self.usernombre.text,
                email=self.useremail.text,
                phone=self.userphone.text,
                source=token1
                
            )

            doc=stripe.Customer.list(limit=1)
            NI=(doc.data[0].id)

            token2= stripe.Token.create(
            card={
                "number": self.usercard.text,
                "exp_month": self.userm.text,
                "exp_year": self.usery.text,
                "cvc": self.usercvv.text,
            }, )
            stripe.Customer.create_source(
                NI,
                source=token2,
                )
            a=stripe.Customer.list(limit=1)
            d=(a.data[0].id)
            stripe.Subscription.create(
            customer=d,
                items=[{"price": "price_1PugPtJTbZoKzQ84CJVuR933"}],
                )


                #stripe.Customer.retrieve()
        except InvalidRequestError as e:
            print(e)
        
        self.usernombre.text=''
        self.userphone.text=''
        self.useraddress.text=''
        self.useremail.text='' 
        self.usercard.text=''
        self.userm.text=''
        self.usery.text=''
        self.usercvv.text=''
        



if __name__ == "__main__":
    AARS().run()
