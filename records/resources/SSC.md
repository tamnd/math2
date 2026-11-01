---
records:
    - id: SSC4C2GGRW
      kind: monograph
      title: 'Carleman Inequalities: An Introduction and More'
      creators:
        - name: Nicolas Lerner
          role: author
      date: "2019"
      msc:
        - code: 35-02
          from: zbmath_search
        - code: 35B45
          from: zbmath_search
        - code: 35B06
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2019"
          ids:
            doi: 10.1007/978-3-030-15993-1
            zbl: "1445.35009"
            zbl_id: "7045638"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer International Publishing
              date: "2019"
              ids:
                isbn:
                    - "9783030159924"
                    - "9783030159931"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-030-15993-1
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "7045638"
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
