---
records:
    - id: RHP5ZNXKPX
      kind: course
      title: Complex Analysis
      creators:
        - name: P. A. S. Sree Krishna
          role: instructor
      date: "2013-11-05"
      ids:
        course: 0022nd079:111103070
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2013-11-05"
          structure: RHP5ZNXKPX/e1.json
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Guwahati
              ids:
                nptel: "111103070"
              access:
                class: record
            - key: m2
              kind: page
              date: "2013-11-05"
              ids:
                nptel: "111103070"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 dev scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111103070"
          level: manifestation
        - source: nptel_video
          snapshot: blake3:7980ec84cfbca0f71922ec2d4e56d2385fa22a44c9cd025088eefbf06b61009d
          native_id: "111103070"
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
    - id: RHPXN7XV60
      kind: monograph
      title: Conformal Dimension
      creators:
        - name: John Mackay
          role: author
        - name: Jeremy Tyson
          role: author
      date: "2010-06-22"
      msc:
        - code: 30-02
          from: zbmath_search
        - code: 30L10
          from: zbmath_search
        - code: 28A78
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010-06-22"
          ids:
            doi: 10.1090/ulect/054
            zbl: "1201.30002"
            zbl_id: "5731476"
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2010-06-22"
              ids:
                isbn:
                    - "9781470416492"
                    - "9780821883105"
                    - "9780821852293"
              access:
                class: record
      relations:
        - kind: part_of
          to: CMK1G7XE8B
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/ulect/054
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "5731476"
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
