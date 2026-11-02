---
records:
    - id: DNG3PTXXM5
      kind: monograph
      title: From Divergent Power Series to Analytic Functions
      creators:
        - name: Werner Balser
          role: author
      date: "1994"
      msc:
        - code: "34E05"
          from: zbmath_search
        - code: 34A25
          from: zbmath_search
        - code: 34-02
          from: zbmath_search
        - code: 34A34
          from: zbmath_search
        - code: 30B10
          from: zbmath_search
        - code: "30E15"
          from: zbmath_search
        - code: 44A10
          from: zbmath_search
        - code: 34M99
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1994"
          ids:
            doi: 10.1007/bfb0073564
            zbl: "0810.34046"
            zbl_id: "637034"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1994"
              ids:
                isbn:
                    - "9783540582687"
                    - "9783540485940"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0073564
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "637034"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: DNGQ82PS4S
      kind: course
      title: Integral and Vector Calculus
      creators:
        - name: Hari Shankar Mahato
          role: instructor
      date: "2019-05-06"
      ids:
        course: 03w5sq511:111105122
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2019-05-06"
          structure: DNGQ82PS4S/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Kharagpur
              ids:
                nptel: "111105122"
              access:
                class: record
            - key: m2
              kind: page
              date: "2019-05-06"
              ids:
                nptel: "111105122"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111105122"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111105122"
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
