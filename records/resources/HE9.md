---
records:
    - id: HE9WM0V7S7
      kind: course
      title: Probability -I with Examples Using R
      creators:
        - name: Siva Athreya
          role: instructor
      date: "2021-01-04"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2021-01-04"
          structure: HE9WM0V7S7/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: ISI Bangalore
              ids:
                nptel: "111106150"
              access:
                class: record
            - key: m2
              kind: page
              date: "2021-01-04"
              ids:
                nptel: "111106150"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106150"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111106150"
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
