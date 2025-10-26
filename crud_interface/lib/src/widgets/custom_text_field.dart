import 'package:flutter/material.dart';

class CustomTextField extends StatelessWidget {
  final String label;
  final TextEditingController controller;

  const CustomTextField({
    super.key,
    required this.label,
    required this.controller,
  });

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 56,
      width: 350,
      child: TextField(
        textAlign: TextAlign.center,
        controller: controller,
        cursorColor: Color.fromRGBO(250, 250, 250, 1),
        style: TextStyle(fontSize: 22, fontFamily: "MonomaniacOne"),
        decoration: InputDecoration(
          filled: true,
          fillColor: Color.fromRGBO(93, 93, 93, 1),
          floatingLabelBehavior: FloatingLabelBehavior.never,
          label: Center(
            child: Text(
              label,
              textAlign: TextAlign.center,
              style: TextStyle(
                fontSize: 20,
                fontFamily: "MonomaniacOne",
                color: Color.fromRGBO(50, 50, 50, 1),
              ),
            ),
          ),
          border: OutlineInputBorder(
            borderRadius: BorderRadius.all(Radius.circular(5)),
          ),
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Color.fromRGBO(250, 250, 250, 1)),
          ),
        ),
      ),
    );
  }
}
