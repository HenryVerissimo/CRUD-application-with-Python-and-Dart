import 'package:crud_interface/app/ui/widgets/custom_button.dart';
import 'package:crud_interface/app/ui/widgets/custom_text_field.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class UpdateUserPage extends StatefulWidget {
  const UpdateUserPage({super.key});

  @override
  State<UpdateUserPage> createState() => UpdateUserPageState();
}

class UpdateUserPageState extends State<UpdateUserPage> {
  var idController = TextEditingController();
  var usernameController = TextEditingController();
  var emailController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Column(
      spacing: 40,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Column(
          children: [
            SvgPicture.asset("assets/images/update_icon.svg", width: 60),
            Text(
              "UPDATE USER",
              style: TextStyle(
                color: Color.fromRGBO(255, 255, 255, 1),
                fontSize: 32,
                fontFamily: "MonomaniacOne",
              ),
            ),
          ],
        ),
        Column(
          spacing: 5,
          children: [
            CustomTextField(label: "ID", controller: idController),
            CustomTextField(label: "USERNAME", controller: usernameController),
            CustomTextField(label: "EMAIL", controller: emailController),
          ],
        ),
        CustomButton(
          icon: Icon(Icons.update, color: Colors.black87),
          text: "UPDATE",
          color: Color.fromRGBO(77, 219, 124, 1),
          onPressed: () {},
        ),
      ],
    );
  }
}
