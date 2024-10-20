import React from "react";
import { Card, CardContent, Typography, Box } from "@mui/material";
const apiUrl = process.env.NEXT_PUBLIC_API_URL;

export default function CenterCard(props) {
  const { center } = props;

  return (
    <Card
      key={center.id}
      sx={{
        display: "flex",
        mb: 2,
        width: "100%",
      }}
    >
      <CardContent>
        <Box
          sx={{
            flex: 0.8,
            width: "100%",
            height: "300px",
            overflow: "hidden",
          }}
        >
          <img
            style={{
              width: "100%",
              maxHeight: "auto",
              borderRadius: "2%",
              aspectRatio: 1,
              objectFit: "cover",
            }}
            alt="Center Photo"
            src={`${apiUrl}/api/images/users/${center.id}/profile`}
          />
        </Box>
        <Box>
          <Typography variant="h5">
            {center.name}, {center.state}
          </Typography>
          <Typography>
            {center.address}, {center.city}
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );
}
