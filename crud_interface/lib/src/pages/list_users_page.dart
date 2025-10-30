import 'package:crud_interface/src/widgets/custom_button.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';

class ListUsersPage extends StatefulWidget {
  const ListUsersPage({super.key});

  @override
  State<ListUsersPage> createState() => ListUsersPageState();
}

class ListUsersPageState extends State<ListUsersPage> {
  List<String> records = [];

  @override
  Widget build(BuildContext context) {
    return Column(
      spacing: 30,
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        Column(
          children: [
            SvgPicture.asset("assets/images/list_icon.svg", width: 60),
            Text(
              "LIST USERS",
              style: TextStyle(
                fontSize: 32,
                color: Colors.white,
                fontFamily: "MonomaniacOne",
              ),
            ),
          ],
        ),
        Container(
          width: 500,
          height: 300,
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: Color.fromRGBO(39, 39, 39, 1),
            borderRadius: BorderRadiusGeometry.all(Radius.circular(10)),
          ),
          child: RawScrollbar(
            thumbVisibility: true,
            thumbColor: Colors.grey,
            child: ListView.builder(
              itemCount: records.length,
              itemBuilder: (context, index) {
                return Text(
                  records[index],
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.white,
                    fontFamily: "MonomaniacOne",
                  ),
                );
              },
            ),
          ),
        ),
        CustomButton(
          icon: Icon(Icons.refresh, color: Colors.black87),
          text: "REFRESH",
          color: Color.fromRGBO(77, 219, 124, 1),
          onPressed: () {},
        ),
      ],
    );
  }
}
