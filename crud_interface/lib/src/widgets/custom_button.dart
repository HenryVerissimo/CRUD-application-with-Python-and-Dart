import 'package:flutter/material.dart';

class CustomButton extends StatelessWidget {
  final Icon icon;
  final String text;
  final Color color;
  final VoidCallback onPressed;

  const CustomButton({
    super.key,
    required this.icon,
    required this.text,
    required this.color,
    required this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: 200,
      height: 40,
      child: FloatingActionButton.extended(
        backgroundColor: color,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadiusGeometry.all(Radius.circular(5)),
        ),
        onPressed: () {},
        label: Column(
          children: [
            Text(
              text,
              style: TextStyle(
                fontFamily: "MonomaniacOne",
                fontSize: 20,
                color: Colors.black87,
              ),
            ),
            SizedBox(height: 4),
          ],
        ),
        icon: icon,
      ),
    );
  }
}
