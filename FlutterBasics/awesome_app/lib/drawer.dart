import 'package:flutter/material.dart';

class MyDrawer extends StatelessWidget {
  const MyDrawer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        children: const <Widget>[
          UserAccountsDrawerHeader(
            accountName: Text("Robert Zaharia"),
            accountEmail: Text("robert@gmail.com"),
            currentAccountPicture: CircleAvatar(
              backgroundImage: NetworkImage(
                  "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1587&q=80"),
            ),
          ),
          ListTile(
            leading: Icon(Icons.person),
            title: Text("Robert Zaharia"),
            subtitle: Text("Developer"),
            trailing: Icon(Icons.edit),
          ),
          ListTile(
              leading: Icon(Icons.email),
              title: Text("Email"),
              subtitle: Text("blabla@gmail.com"),
              trailing: Icon(Icons.edit)),
        ],
      ),
    );
  }
}
