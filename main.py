from formularios.Login.form_login import FormLogin
import build_db

if __name__ == '__main__':
    build_db.app_build()
    app = FormLogin()
    app.mainloop()
