---
records:
    - id: 9SH0WM7954
      kind: course
      title: Engineering Mathematics - I
      creators:
        - name: Jitendra Kumar
          role: instructor
      date: "2019-05-06"
      msc:
        - code: 00-XX
          from: classify/1@2b838f8bc9d8
      ids:
        course: 03w5sq511:111105121
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2019-05-06"
          structure: 9SH0WM7954/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Kharagpur
              ids:
                nptel: "111105121"
              access:
                class: record
            - key: m2
              kind: page
              date: "2019-05-06"
              ids:
                nptel: "111105121"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111105121"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111105121"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
---
