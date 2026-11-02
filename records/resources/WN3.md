---
records:
    - id: WN38789HTP
      kind: monograph
      title: Einführung in die Analytische Zahlentheorie
      creators:
        - name: K. Chandrasekharan
          role: author
      date: "1966"
      msc:
        - code: 11-02
          from: zbmath_search
        - code: 11Hxx
          from: zbmath_search
        - code: 11Jxx
          from: zbmath_search
        - code: 11Mxx
          from: zbmath_search
        - code: 11Nxx
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: de
          date: "1966"
          ids:
            doi: 10.1007/bfb0082655
            zbl: "0154.04402"
            zbl_id: "3247296"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1966"
              ids:
                isbn:
                    - "9783540036111"
                    - "9783540348559"
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
          native_id: 10.1007/bfb0082655
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3247296"
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
          at: "2026-11-02"
          by: m2 dev scope/1
          note: from in to in
---
