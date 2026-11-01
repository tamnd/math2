---
records:
    - id: RT6DDTXMKJ
      kind: monograph
      title: Postmodern Analysis
      creators:
        - name: Jürgen Jost
          role: author
      date: "1998"
      msc:
        - code: 26-01
          from: zbmath_search
        - code: 46-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1998"
          ids:
            doi:
                - 10.1007/978-3-662-03635-8
                - 10.1007/978-3-662-05306-5
            zbl: "0971.26001"
            zbl_id: "1110787"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1998"
              ids:
                isbn:
                    - "9783540634850"
                    - "9783662036358"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2003"
              ids:
                isbn:
                    - "9783540438731"
                    - "9783662053065"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-03635-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-05306-5
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1110787"
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
