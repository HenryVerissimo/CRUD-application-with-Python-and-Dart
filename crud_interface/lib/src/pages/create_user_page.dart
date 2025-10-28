import 'package:crud_interface/src/widgets/custom_button.dart';
import 'package:crud_interface/src/widgets/custom_text_field.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class CreateUserPage extends StatefulWidget {
  const CreateUserPage({super.key});

  @override
  State<CreateUserPage> createState() => CreateUserPageState();
}

class CreateUserPageState extends State<CreateUserPage> {
  var userNameController = TextEditingController();
  var emailController = TextEditingController();
  var passwordController = TextEditingController();
  var confirmPasswordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Column(
      spacing: 40,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Column(
          children: [
            SvgPicture.asset("assets/images/create_user_icon.svg", width: 60),
            Text(
              "CREATE USER",
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
            CustomTextField(label: "USERNAME", controller: userNameController),
            CustomTextField(label: "EMAIL", controller: emailController),
            CustomTextField(label: "PASSWORD", controller: passwordController),
            CustomTextField(
              label: "CONFIRM PASSWORD",
              controller: confirmPasswordController,
            ),
          ],
        ),
        CustomButton(
          icon: Icon(Icons.add, color: Colors.black87),
          text: "CREATE",
          color: Color.fromRGBO(77, 219, 124, 1),
          onPressed: () {},
        ),
      ],
    );
  }
}
