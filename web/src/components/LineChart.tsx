import { Card } from "@mui/material";
import React from "react";
import { Line } from "react-chartjs-2";
import "./css/line-chart.scss";

export const LineChart = () => {
  return (
    <Card
      className="line-chart"
      style={{ boxShadow: "0px 2px 50px rgba(0, 0, 0, 0.1)" }}
    >
      <h3 className="line-chart__title">腕立て伏せ</h3>
      <div style={{ width: 400, height: 210 }}>
        <Line
          data={{
            labels: ["1", "2", "3", "4", "5", "6"],
            datasets: [
              {
                label: "# of Votes",
                data: [12, 30, 3, 5, 2, 3],
                fill: false,
                backgroundColor: "rgb(255, 99, 132)",
                borderColor: "rgba(255, 99, 132, 0.2)",
              },
            ],
          }}
        />
      </div>
    </Card>
  );
};
