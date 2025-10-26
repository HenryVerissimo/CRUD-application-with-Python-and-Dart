import 'package:crud_interface/src/pages/create_user_page.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(MyAPP());
}

class MyAPP extends StatelessWidget {
  const MyAPP({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        scaffoldBackgroundColor: Color.fromRGBO(51, 51, 51, 1),
        textSelectionTheme: TextSelectionThemeData(
          selectionColor: Color.fromRGBO(250, 250, 250, 0.8),
        ),
      ),
      home: CreateUserPage(),
    );
  }
}
