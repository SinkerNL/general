import 'package:awesome_app/pages/home_page.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);
  static const String routeName = "/login";
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final formKey = GlobalKey<FormState>();
  final _usernameController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: Text("Login Page"), actions: [
          IconButton(onPressed: () {}, icon: Icon(Icons.exit_to_app))
        ]),
        body: Stack(
          fit: StackFit.expand,
          children: [
            Image.asset(
              "coding.jpg",
              fit: BoxFit.cover,
              color: Colors.black.withOpacity(0.7),
              colorBlendMode: BlendMode.darken,
            ),
            Center(
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: SingleChildScrollView(
                    child: SingleChildScrollView(
                  child: Form(
                    key: formKey,
                    child: Card(
                      child: Padding(
                        padding: const EdgeInsets.all(16.0),
                        child: Column(
                          children: <Widget>[
                            TextFormField(
                                controller: _usernameController,
                                keyboardType: TextInputType.emailAddress,
                                validator: (s) {},
                                decoration: InputDecoration(
                                    hintText: "Enter email",
                                    labelText: "Username")),
                            SizedBox(height: 20),
                            TextFormField(
                                controller: _passwordController,
                                keyboardType: TextInputType.text,
                                validator: (s) {},
                                obscureText: true,
                                decoration: InputDecoration(
                                    hintText: "Enter password",
                                    labelText: "Password")),
                            SizedBox(height: 20),
                            RaisedButton(
                              onPressed: () {
                                //formKey.currentState.validate();
                                Navigator.push(
                                    context,
                                    MaterialPageRoute(
                                        builder: (context) => HomePage()));
                              },
                              child: Text("Sign In"),
                              color: Colors.orange,
                              textColor: Colors.white,
                            )
                          ],
                        ),
                      ),
                    ),
                  ),
                )),
              ),
            )
          ],
        ));
  }
}
