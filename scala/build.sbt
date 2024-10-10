// Project name
name := "atlas-data"

// Project version
version := "0.1.0"

// Scala version
scalaVersion := "2.12.13"  // You can update this version as needed

// Library dependencies
libraryDependencies ++= Seq(
  // Example: Add your dependencies here
  "org.scala-lang" %% "scala-library" % scalaVersion.value,
  "org.scalatest" %% "scalatest" % "3.2.16" % Test,
  "com.typesafe.akka" %% "akka-actor-typed" % "2.6.20" // Example Akka dependency
)

// Add any other project settings here
scalacOptions ++= Seq(
  "-deprecation",      // Emit warning and location for usages of deprecated APIs.
  "-feature",          // Emit warning and location for usages of features that should be imported explicitly.
  "-unchecked",        // Enable additional warnings where generated code depends on assumptions.
  "-Xfatal-warnings"   // Fail the compilation if there are any warnings.
)