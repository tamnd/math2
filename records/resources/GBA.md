---
records:
    - id: GBA32PSBH2
      kind: course
      title: Commutative Algebra with a Viewpoint towards Algebraic Number Theory
      creators:
        - name: Bharathwaj Palvannan
          role: instructor
      date: "2026-06-18"
      ids:
        course: 04dese585:111108003
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2026-06-18"
          structure: GBA32PSBH2/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: IISc Bangalore
              ids:
                nptel: "111108003"
              access:
                class: record
            - key: m2
              kind: page
              date: "2026-06-18"
              ids:
                nptel: "111108003"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111108003"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111108003"
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
    - id: GBA99REJKR
      kind: monograph
      title: Fields, Flows and Waves
      creators:
        - name: David F. Parker
          role: author
      date: "2003"
      msc:
        - code: 00A05
          from: zbmath_search
        - code: 35-01
          from: zbmath_search
        - code: 74-01
          from: zbmath_search
        - code: 76-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2003"
          ids:
            doi: 10.1007/978-1-4471-0019-5
            zbl: "1016.00001"
            zbl_id: "1930451"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2003"
              ids:
                isbn:
                    - "9781852337087"
                    - "9781447100195"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4471-0019-5
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "1930451"
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
---
