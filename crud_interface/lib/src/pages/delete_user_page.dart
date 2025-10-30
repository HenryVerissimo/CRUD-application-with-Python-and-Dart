import 'package:crud_interface/src/widgets/custom_button.dart';
import 'package:crud_interface/src/widgets/custom_text_field.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';

class DeleteUserPage extends StatefulWidget {
  const DeleteUserPage({super.key});

  @override
  State<DeleteUserPage> createState() => DeleteUserPageState();
}

class DeleteUserPageState extends State<DeleteUserPage> {
  var idController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Column(
      spacing: 40,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Column(
          children: [
            SvgPicture.asset("assets/images/trash_icon.svg", width: 60),
            Text(
              "DELETE USER",
              style: TextStyle(
                color: Color.fromRGBO(255, 255, 255, 1),
                fontSize: 32,
                fontFamily: "MonomaniacOne",
              ),
            ),
          ],
        ),
        CustomTextField(label: "ID", controller: idController),
        CustomButton(
          icon: Icon(Icons.delete, color: Colors.black87),
          text: "DELETE",
          color: Color.fromRGBO(219, 77, 101, 1),
          onPressed: () {},
        ),
      ],
    );
  }
}
